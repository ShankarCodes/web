import pymongo
from bson.objectid import ObjectId

class MDB:
    def __init__(self,dbname,collection_name):
        self.dbname = dbname
        self.collection_name = collection_name
        self.client = pymongo.MongoClient()
        self.db = self.client[self.dbname]
        self.collection = self.db[self.collection_name]
    
    def insert(self,data):
        id_ = self.collection.insert_one(data).inserted_id
        return id_

    def insert_all(self,data):
        result = self.collection.insert_many(data)
        return result.id_

    def collections(self):
        return self.db.list_collection_names()
    
    def get(self,query=None):
        if query is None:
            return self.collection.find_one()
        else:
            return self.collection.find_one(query)
    
    def get_by_id(self,id_):
        return self.collection.find_one({'_id': ObjectId(post_id)})

    def get_all(self,query=None):
        if query is None:
            return self.collection.find()
        else:
            return self.collection.find(query)
    def create_index(self,index_name,unique_value=True):
        self.collection.create_index([(index_name, pymongo.ASCENDING)],unique=unique_value)

    def count(self,query):
        return self.collection.count_documents(query)


        



    
    
