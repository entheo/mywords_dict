from . import api
from django.http import JsonResponse


dict = api.YouDao()
res = {}


def trans(request):
    if request.method == 'GET':
        word = request.GET['word']
        res['trans'] = dict.get_trans(word)
        res['pronounce'] = dict.get_pronounce(word)
        return JsonResponse({'res':res})