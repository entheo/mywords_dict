from mongodb import Memo, User, Dict
from django.http import JsonResponse
from dict.api import YouDao
import json

# 创建Memo
def create(request):
    if request.method == 'POST':
        print(request.POST)
    pass

# 添加到Memo,同时在Dict进行备份
def add(request):

    open_id = json.loads(request.body.decode('utf-8'))['open_id']
    word = json.loads(request.body.decode('utf-8'))['word']
    u = User()
    u.check_user(open_id)
    m = Memo()
    res = m.add(open_id, word)

    # 备份trans
    dict_source = YouDao()
    info = dict_source.get_trans_pronounce(word)
    d = Dict()
    d.create(word, info['trans'], info['pronounce'])

    return JsonResponse({'res': res})


# 获得已有Memo
def find(request):
    if request.method == 'POST':
        open_id = json.loads(request.body.decode('utf-8'))['open_id']
        m = Memo()
        memo = m.find(open_id)
        if memo:
            return JsonResponse({'words': memo['words']})
        else:
            return False


# 获取一个用户的生词字典
def get_memo_dict(request):
    if request.method == 'POST':
        open_id = json.loads(request.body.decode('utf-8'))['open_id']
        res = []
        m = Memo()
        d = Dict()
        memo = m.find(open_id)
        print(memo, memo['words'], open_id)
        if memo and memo['words']:
            for w in memo['words']:
                word = d.col.find_one({'word': w}, {'word': 1, 'trans': 1, 'pronounce': 1, '_id': 0})

                # 将word的trans数量限制在三个以内
                trans = word['trans']
                trans.sort(key=lambda i: len(i))
                if len(trans) > 3:
                    word['trans'] = trans[0:2]

                res.append(word)
            return JsonResponse({'dict': res})
        else:
            return JsonResponse({'dict': []})


# 从一个用户的memo中删除对应单词
def delete_memo_word(request):
    if request.method == 'POST':
        open_id = json.loads(request.body.decode('utf-8'))['open_id']
        word = json.loads(request.body.decode('utf-8'))['word']
        print(word)
        m = Memo()
        if m.find(open_id):
            m.delete_word(word, open_id)
            return JsonResponse({'res': True})
        else:
            return JsonResponse({'res': False})
