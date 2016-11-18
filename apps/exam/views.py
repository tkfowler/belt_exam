from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
# Create your views here.
def index(request):
    return render(request, 'exam/index.html')

def login(request):
    result = User.objects.validateLogin(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])

def register(request):
    result = User.objects.validateReg(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])

def home(request):
    if not 'user' in request.session:
        return redirect('/')
    context = {
        'items': Item.objects.all(),
        'user' : User.objects.all(),
        'other': Item.objects.all().order_by('-id')[:4]
    }

    return render(request, 'exam/home.html', context)

def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'name' : user.name,
        'username' : user.username,
        'date' : user.date,
    }
    return redirect('/home')

def logout(request):
    request.session.pop('user')
    return redirect('/')

def add(request):
    return render(request, 'exam/add.html')

def create(request):
    Item.objects.create(name=request.POST['item'])
    return redirect('/home')

def delete(request, id):
    Item.objects.filter(id=id).delete()
    return redirect('/home')

def item(request, id):
    context = {
    'item' : Item.objects.get(id=id),
    'user' : Item.objects.get(id=id)
    }
    return render(request, 'exam/show.html', context)

# def move(request, id):
#     item = Item.objects.filter(id=id)
#     if item:
#         ietem
