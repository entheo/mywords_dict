from mongodb import User, Memo
import requests
import hmac
from django.http import JsonResponse

# 从微信服务器标识用户登录，并获取用户对应的session_key与openid
def wx_login(code):
    appsecret= 'c4f162ae7f6d38d80b99fd543ad4128d'
    appid = 'wxf5968a2e5202ed42'
    url = 'https://api.weixin.qq.com/sns/jscode2session?appid='+appid+'&secret='+appsecret+'&js_code='+code+'&grant_type=authorization_code'
    res = requests.get(url)
    open_id = res.json()['openid']
    session_key = res.json()['session_key']
    return {
        'open_id':open_id,
        'session_key':session_key
    }


# 判断是否已注册
def is_user(open_id):
    u = User()
    user = u.col.find_one({'open_id': open_id})
    if user:
        return user
    return False



# 小程序用户在后台登录获取token
def login(request):
    res = {}
    if request.method == 'POST':
        code = request.POST['code']
        print('获取code：', code)
        wx = wx_login(code)
        u = User()
        u.create(wx['open_id'])
        m = Memo()
        m.create(wx['open_id'])
        res['open_id'] = wx['open_id']
    return JsonResponse(res)

'''
暂时取消，不需要登录态，直接采用openid来自识别用户
# 生成用户身份token，用来在小程序前端识别登录态
def generate_token(session_key,openid):
    h = hmac.new(session_key.encode('utf-8'), openid.encode('utf-8'), digestmod='MD5')
    return h.hexdigest()
'''
