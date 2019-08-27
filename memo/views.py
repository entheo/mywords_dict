from mongodb import Memo
from django.http import JsonResponse
import json

# 创建Memo
def create(request):
    if request.method == 'POST':
        print(request.POST)
    pass

# 添加到Memo
def add(request):
    print(request.body)
    open_id = json.loads(request.body.decode('utf-8'))['open_id']
    word = json.loads(request.body.decode('utf-8'))['word']
    m = Memo()
    m.add(open_id, word)
    return JsonResponse({'res':'成功加入'})

# 获得已有Memo
def find (request):
    if request.method == 'POST':
        open_id = json.loads(request.body.decode('utf-8'))['open_id']
        m = Memo()
        memo = m.find(open_id)
        return JsonResponse({'words': memo['words']})