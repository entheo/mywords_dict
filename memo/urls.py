from django.urls import path
from . import views

urlpatterns = {
    path('create', views.create, name='create'),
    path('add', views.add, name='add'),
    path('find', views.find, name='find')
}