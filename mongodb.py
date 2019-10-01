import pymongo
import datetime

def now():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

class Data():
    def __init__(self):
        # root登录mongodb
        self.client = pymongo.MongoClient('mongodb://root:2810033@localhost:27017')
        self.db = self.client['mywords_dict']

        # entheo登录mywordict
        self.client.mywords_dict.authenticate('entheo', '2810033')


class User(Data):
    def __init__(self):
        super(User,self).__init__()
        self.col = self.db['user']

    def create(self, openid):
        if not self.is_user(openid):
            self.col.insert_one({'open_id': openid, 'created_at':now()})
        else:
            return False

    def is_user(self, openid):
        if self.col.find_one({'open_id': openid}):
            return True
        else:
            return False

    # 如果没有用户，那么添加
    def check_user(self,openid):
        if not self.is_user(openid):
            self.create(openid)
            m = Memo()
            m.create(openid)


class Memo(Data):
    def __init__(self):
        super(Memo,self).__init__()
        self.col = self.db['memo']

    def create(self, openid):
        words = []
        if not self.find(openid):
            self.col.insert_one({'open_id': openid, 'words': words, 'created_at': now()})
        else:
            return False

    def add(self, openid, word):
        # 检查生词是否已存在, 如果没有添加，否则返回已存在状态
        already_has_word = self.check_word(word, openid)
        if not already_has_word:
            new_words = self.find(openid)['words']
            new_words.append(word)
            self.col.update_one({'open_id': openid}, {'$set': {'words': new_words, 'updated_at': now()}})
            return True

        else:
            return False

    # 查找对应用户的生词本
    def find(self, openid):
        memo = self.col.find_one({'open_id': openid})
        if memo:
            return memo
        else:
            words = []
            self.col.insert_one({'open_id': openid, 'words': words, 'created_at': now()})
            print('新建完成')
            memo = self.col.find_one({'open_id': openid})
            return memo


    # 检查单词是否已存在
    def check_word(self, word, openid):
        m = self.find(openid)
        if word in m['words']:
            return True
        else:
            return False

    #获取生词列表
    def get_memo_words(self, openid):
        m = self.find(openid)
        words = m['words']
        return words

    # 删除对应单词
    def delete_word(self, word, openid):
        words = self.get_memo_words(openid)
        print('memo为：', words)
        if word in words:
            words.remove(word)
            if not words:
                words = []
            my_query = {'open_id': openid}
            new_value = {'$set': {'words': words}}
            new_m = self.col.update_one(my_query, new_value)
            return new_m
        else:
            return False


class Dict(Data):
    def __init__(self):
        super(Dict, self).__init__()
        self.col = self.db['dict']

    # trans 为list类型
    def create(self, word, trans, pronounce):
        if not self.find_word(word):
            self.col.insert_one({'word':word, 'trans':trans, 'pronounce':pronounce, 'created_at':now()})
            return True

    # 查询单词是否存在
    def find_word(self,word):
        if self.col.find_one({'word': word}):
            return True
        else:
            return False


# 词库
class WordList(Data):
    def __init__(self):
        super(WordList, self).__init__()
        self.col = self.db['word_list']

    def find_name(self, name):
        if self.col.find_one({'name': name}):
            return True
        else:
            return False

    def create(self, name, word_list):
        if not self.find_name(name):
            self.col.insert_one({'name': name, 'word_list': word_list, 'created_at': now()})
            return True

    def find(self, name):
        res = self.col.find_one({'name': name})
        return res








