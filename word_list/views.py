from django.shortcuts import render
from mongodb import WordList
from django.http import JsonResponse
import json

# Create your views here.

word_list = WordList()


#获取雅思精选词汇
def get_word_list(request):
    if request.method == 'POST':
        name = json.loads(request.body.decode('utf-8'))['name']
        print(name)
        res = word_list.find(name)['word_list']
        return JsonResponse({'word_list': res})


