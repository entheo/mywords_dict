import pymongo

class Data():

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['mywords_dict']


class Memo(Data):

    def __init__(self):
        super(Memo,self).__init__()
        self.col = self.db['memo']

    def create(self,openid):
        words = []
        self.col.insert_one({'open_id': openid, 'words':words})