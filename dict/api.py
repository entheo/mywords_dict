'''抓取有道词典的查询接口'''
import requests
from bs4 import BeautifulSoup

def get_trans(word):
    trans = []
    url = 'http://dict.youdao.com/w/eng/'+word+'/#keyfrom=dict2.index'
    res = requests.get(url)
    soup = BeautifulSoup(res.content,'html.parser')
    t_list = soup.find('div',class_='trans-container').find('ul')
    for i in t_list:
        if i != '\n':
            trans.append(i.string)
    return trans

   
   
