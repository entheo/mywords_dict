from . import api
from django.http import JsonResponse

d = api.YouDao()
c = api.DictCn()
res = {}


# 辨别是否含有中文
def is_chinesee(uchar):
    if '\u4e00' <= uchar <= '\u9fff':
        return True
    else:
        return False


def get_trans(word):
    res = {}
    if is_chinesee(word):
        res['trans'] = d.ch_trans(word)
        res['language'] = 'ch'
    else:
        res['trans'] = d.get_trans(word)
        res['pronounce'] = d.get_pronounce(word)
        res['language'] = 'en'
        res['sentences'] = c.get_sentences(word)
    return res


def trans(request):
    if request.method == 'GET':
        return JsonResponse({'res': get_trans(request.GET['word'])})
