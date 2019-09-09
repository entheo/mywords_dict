from django.urls import path
from . import views

urlpatterns = {
    path('create', views.create, name='create'),
    path('add', views.add, name='add'),
    path('find', views.find, name='find'),
    path('get_memo_dict', views.get_memo_dict, name='get_memo_dict')
}