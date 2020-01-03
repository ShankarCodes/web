import pymongo
from bson.objectid import ObjectId
import json 
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
        return self.collection.find_one({'_id': ObjectId(id_)})

    def get_many(self,query=None):
        if query is None:
            return self.collection.find()
        else:
            return self.collection.find(query)
    def create_index(self,index_name,unique_value=True):
        self.collection.create_index([(index_name, pymongo.ASCENDING)],unique=unique_value)

    def count(self,query):
        return self.collection.count_documents(query)

    def update(self,query,newdata):
        self.collection.update_one(query,{'$set':newdata})
    
    def add(self,query,newdata):
        self.collection.update_one(query,{'$push':newdata})
    
    def add_many(self,query,field,data):
        self.collection.update_one(query,{"$push":{field:{"$each":data}}})


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

        



    
    
