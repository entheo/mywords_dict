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
        try:
            memo = self.col.find_one({'open_id': openid})
        except LookupError:
            print('用户的生词本不存在')
            return False
        else:
            return memo

    # 检查单词是否已存在
    def check_word(self, word, openid):
        m = self.find(openid)
        if word in m['words']:
            return True
        else:
            return False









