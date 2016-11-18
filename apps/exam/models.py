from __future__ import unicode_literals
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import bcrypt, re
from datetime import datetime

class UserManager(models.Manager):
    def validateReg(self, request):
        errors = self.validate_inputs(request)

        if len(errors) > 0:
            return (False, errors)

        # No errors, time to hash the pw
        pw_hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())

        # pw is hashed, time to create new user
        user = self.create(name=request.POST['name'], username=request.POST['username'], date=request.POST['date'], pw_hash=pw_hash)

        return (True, user)

    def validateLogin(self, request):
        try:
            user = User.objects.get(username=request.POST['username'])
            password = request.POST['password'].encode()
            if bcrypt.hashpw(password, user.pw_hash.encode()):
                return (True, user)

        except ObjectDoesNotExist:
            pass

        return (False, ["Username/password don't match."])

    def validate_inputs(self, request):
        errors = []
        if len(request.POST['name']) < 1 or len(request.POST['username']) < 1:
            errors.append("Please include a name and/or username longer than two characters.")
        if len(request.POST['password']) < 8 or request.POST['password'] != request.POST['confirm_pw']:
            errors.append("Passwords must match and be at least 8 characters.")

        return errors

class User(models.Model):
    name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    pw_hash = models.CharField(max_length=255)
    date = models.CharField(max_length=50)

    objects = UserManager()

class Item(models.Model):
    name = models.CharField(max_length=50)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Wishlist(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
