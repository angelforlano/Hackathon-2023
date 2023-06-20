from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from gridfs import GridFS

class Database():
    client = None
    
    def __init__(self, name:str, cluster:str, develop = False, logging = True) -> None:
        
        # save the mongoDB client as a singleton, to re use on other clases
        if(Database.client == None):
            Database.client = MongoClient("mongodb+srv://superhacker2013:{}@test.5hm29hp.mongodb.net/?retryWrites=true&w=majority".format("TrTjmdTk3lq70KfX", cluster), server_api=ServerApi('1'))
            Database.databases = {}
        
        self.name = f'{name}_develop' if develop else name
        self.database = self.client[self.name]
        self.logging = logging
        self.collections = {}
        self.grid_fs = GridFS(self.database, collection="fs")
        
        Database.instance = self
        Database.databases[self.name] = self
        pass
    
    def insert(self, data, into = None):
        result = self.database[self.set_into(into)].insert_one(data)
        
        if (result != None):
            return str(result.inserted_id)
        raise AttributeError("Inserted object couldn't be completed")