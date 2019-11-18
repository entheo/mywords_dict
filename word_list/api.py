from bs4 import BeautifulSoup
import requests


# 新东方IELTS精选词库
class JingXuan():
    def __init__(self):
      self.base_url = 'https://www.koolearn.com/dict/tag_769_'

    def get_word_list(self):
      i = 1
      word_list = []
      while i < 10:
        url = self.base_url+str(i)+'.html'
        res = requests.get(url)
        soup = BeautifulSoup(res.content,'html.parser')
        p_words_list = soup.find('div', class_='word-box').find_all('a')
        for w in p_words_list:
            word_list.append(w.string)
        i += 1
      return word_list


#新东方四级词库
class Siji():
    def __init__(self):
        self.base_url = 'https://www.koolearn.com/dict/tag_365_'

    def get_word_list(self):
        i = 1
        word_list = []
        while i < 20:
            url = self.base_url+str(i)+'.html'
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            p_words_list = soup.find('div', class_='word-box').find_all('a')
            for w in p_words_list:
                word_list.append(w.string)
            i += 1
        return word_list


#新东方六级必备词汇
class Liuji():
    def __init__(self):
        self.base_url = 'https://www.koolearn.com/dict/tag_381_'

    def get_word_list(self):
        i = 1
        word_list = []
        while i < 10:
            url = self.base_url+str(i)+'.html'
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            p_words_list = soup.find('div', class_='word-box').find_all('a')
            for w in p_words_list:
                word_list.append(w.string)
            i += 1
        return  word_list
