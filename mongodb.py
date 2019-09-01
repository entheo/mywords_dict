import pymongo


class Data():
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['mywords_dict']


class User(Data):
    def __init__(self):
        super(User,self).__init__()
        self.col = self.db['user']

    def create(self, openid):
        self.col.insert_one({'open_id': openid})

    def is_user(self,openid):
        if self.col.find_one({'open_id':openid}):
            return
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
        self.col.insert_one({'open_id': openid, 'words':words})

    def add(self,openid,word):
        u = self.col.find_one({'open_id':openid})
        print('被添加用户:', u)
        if u['words']:
            new_words = u['words']
            if word not in new_words:
                new_words.append(word)
        else:
            new_words = []
            new_words.append(word)
        self.col.update_one({'open_id':openid}, {'$set': {'words': new_words}})
        return True

    def find(self,openid):
        m = self.col.find_one({'open_id': openid})
        return m



