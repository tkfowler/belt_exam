from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^home$', views.home),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^create$', views.create),
    url(r'^delete/(?P<id>\d+)$', views.delete),
    url(r'^item/(?P<id>\d+)$', views.item),
]
