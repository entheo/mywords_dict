'''抓取有道词典的查询接口'''
import requests
from bs4 import BeautifulSoup

class YouDao():
    def __init__(self):
        self.url = 'http://dict.youdao.com/w/eng/'

   # 抓取网页结构
    def get_soup(self, word):
        res = requests.get(self.url+word)
        soup = BeautifulSoup(res.content,'html.parser')
        return soup


    # 抓取单词解释
    def get_trans(self, word):
        trans = []
        t_list = self.get_soup(word).find('div',class_='trans-container').find('ul')
        if t_list:
            for i in t_list:
                if i != '\n':
                    trans.append(i.string)
            return trans
        else:
            return False

    # 抓取英美音标
    def get_pronounce(self,word):
        res = {}
        p_list = self.get_soup(word).find_all('span',class_='pronounce')
        if p_list:
            res['uk'] = p_list[0].find('span').string
            res['us'] = p_list[1].find('span').string
            return res
        else:
            return False


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


