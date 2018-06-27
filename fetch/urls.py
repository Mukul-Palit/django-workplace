from django.urls import path
from . import views
from .models import Group
from django.views.generic import ListView, DetailView

urlpatterns = [
    path('', views.home, name='home'),
    path('group/', views.group, name='group'),
    path('members/', views.members, name='members'),
]