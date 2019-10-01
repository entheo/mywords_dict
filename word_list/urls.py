from django.urls import path
from . import views

urlpatterns = {
    path('get_word_list', views.get_word_list)
}
