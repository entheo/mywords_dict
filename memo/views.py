from mongodb import Memo, User
from django.http import JsonResponse
import json

# 创建Memo
def create(request):
    if request.method == 'POST':
        print(request.POST)
    pass

# 添加到Memo
def add(request):

    open_id = json.loads(request.body.decode('utf-8'))['open_id']
    word = json.loads(request.body.decode('utf-8'))['word']
    u = User()
    u.check_user(open_id)
    m = Memo()
    m.add(open_id, word)
    return JsonResponse({'res':'成功加入生词库'})

# 获得已有Memo
def find (request):
    if request.method == 'POST':
        open_id = json.loads(request.body.decode('utf-8'))['open_id']
        m = Memo()
        memo = m.find(open_id)
        return JsonResponse({'words': memo['words']})
