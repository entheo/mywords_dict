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


    # 抓取英文单词解释
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
            if len(p_list) == 1:
                if p_list[0].find('span'):
                    res['us'] = p_list[0].find('span').string
            else:
                if p_list[0].find('span'):
                    res['uk'] = p_list[0].find('span').string
                    if p_list[1].find('span'):
                        res['us'] = p_list[1].find('span').string
            return res
        else:
            return False

    # 返回音标与翻译
    def get_trans_pronounce(self,word):
        res = {}
        res['word'] = word
        res['trans'] = self.get_trans(word)
        res['pronounce'] = self.get_pronounce(word)
        return res

    # 抓取中文结果
    def ch_trans(self,word):
        res = []
        container_items = self.get_soup(word).find('div', id='phrsListTab').find_all('div', class_='trans-container')
        if container_items:
            for c in container_items:
                items = c.find_all('span', class_='contentTitle')
                if items:
                    for i in items:
                        res.append(i.find('a').string)
        return res

# www.dict.cn
class DictCn():
    def __init__(self):
        self.url = 'http://www.dict.cn/'

    def get_soup(self, word):
        res = requests.get(self.url+word)
        soup = BeautifulSoup(res.content, 'html.parser')
        return soup

    # 抓取例句
    def get_sentences(self, word):
        s_list = []
        soup = self.get_soup(word)
        s_html = soup.find('div', class_='layout sort').find_all('ol')
        i = 0
        while i < len(s_html):
            for s in s_html[i].find_all('li'):
                c = s.contents
                c.pop(1)
                s_list.append(c)
            i += 1
        return s_list


