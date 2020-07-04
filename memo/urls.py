from django.urls import path
from . import views

urlpatterns = {
    path('create', views.create, name='create'),
    path('add', views.add, name='add'),
    path('find', views.find, name='find'),
    path('get_user_memo_dict', views.get_user_memo_dict, name='get_user_memo_dict'),
    path('delete_memo_word', views.delete_memo_word)
}