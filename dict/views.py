from . import api
from django.http import JsonResponse

def trans(request):
    if request.method == 'GET':
        word = request.GET['word']
        res = api.get_trans(word)
        return JsonResponse({'res':res})