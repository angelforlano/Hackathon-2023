import json
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from gridfs import GridFS
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

# Querys Usase!
# "$gt" (>=), "$lt" (<=)
# resultado = coleccion.find({"$and": [{"campo1": 55}, {"campo2": "valor2"}]})
# resultado = coleccion.find({"$or": [{"campo1": 55}, {"campo2": "valor2"}]})
# {"i.c": {"$gt": 39, "$lt": 60} }
 
class Database():
    client = None
    
    """
    # Command Logger Class
    class CommandLogger(monitoring.CommandListener):
        def started(self, event):
            #print("Started Command {0.command_name} with request id ""{0.request_id} started on server ""{0.connection_id}".format(event))
            pass
        def succeeded(self, event):
            #print("succeeded command {0.command_name} with request id ""{0.request_id} on server {0.connection_id} ""succeeded in {0.duration_micros} ""microseconds".format(event))
            if (event.command_name == "insert"):
                #print("On Insert")
                pass"""
            
    def get_logging_value(obj):
        return obj.logging
    
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
    
    def __getitem__(self, indice):
        if not (indice in self.collections):
            self.collections[indice] = self.database[indice]
        return self.collections[indice]
    
    def set_into(self, into):
        return self.name if into == None else into
    
    def get_collection(self, collname):
        return self.database[collname]
    
    def insert(self, data, into = None):
        result = self.database[self.set_into(into)].insert_one(data)
        if (result != None):
            return str(result.inserted_id)
        raise AttributeError("Inserted object couldn't be completed")
    
    def find_one(self, filter, into = None):
        return self.database[self.set_into(into)].find_one(filter)
    
    def find(self, filter = {}, into = None, limit = 0, order = -1, sort_by = "CT.T"):
        results = None
        try:
            results = self.database[self.set_into(into)].find(filter).sort(sort_by, order).limit(limit)
        except Exception as e:
            results = self.database[self.set_into(into)].find(filter)
        return results
    
    def exist_by_value(self, filter):
        return self.find_one(filter) != None
    
    def exist_by_ID(self, ID, into = None):
        if len(ID) != 24: return None
        return self.exist_by_value({'_id': ObjectId(ID)}, into = into)

    def find_by_ID(self, ID:str, into = None):
        if len(ID) != 24: return None
        return self.find_one({'_id': ObjectId(ID)}, into = into) 

    def update_one(self, filter, data, into = None):
        return self.database[self.set_into(into)].update_one(filter, {"$set": data})

    def update_one_by_ID(self, ID:str, data, into = None) -> bool:
        if len(ID) != 24: return None
        update_result = self.database[self.set_into(into)].update_one({"_id": ObjectId(ID)}, {"$set": data})
        return update_result.modified_count == 1

    def get_count(self, into = None):
        return self.database[self.set_into(into)].count_documents({})
    
    def get_last_document(self, into = None, sort_by = "", return_value:str = "") :
        result = self.find({}, into=into).sort(sort_by, -1).limit(1)
        if result == None:
            return
        return result[0] if return_value == "" else result[0][return_value]

    def delete_one_by_ID(self, ID:str, into = None):
        if len(ID) != 24: return None
        removed_result = self.database[self.set_into(into)].delete_one({"_id": ObjectId(ID)})
        return removed_result.deleted_count == 1
    
    def auto_increment_by_id(self, ID:str, value_name:str, amount:float, into = None):
        if len(ID) != 24: return None
        
        sequence_document = self.database[self.set_into(into)].find_one_and_update(
        {'_id': ObjectId(ID)},
        {'$inc': {value_name: amount}},
            return_document=True
        )
        
        return sequence_document
        
    #####################################################
    ##########      DATABASE FILE SYSTEM       ##########
    #####################################################
    
    def get_all_files(self, filter = None):
        return list(self.grid_fs.find(filter))

    def get_files_count(self, filter = None):
        return len(self.get_all_files(filter))

    def find_file(self, ID:str):
        return self.grid_fs.find_one({'_id': ObjectId(ID)})
    
    def find_file_by_name(self, name:str):
        return self.grid_fs.find_one({'N': name})
    
    def upload_file(self, filename:str, data:bytes, owner_id:str):
        _filename = secure_filename(filename)
        _exten = _filename.split(".")[-1]

        return self.grid_fs.put(data, CT = TimeDim().utc_now(), N = _filename, E = _exten, OID = owner_id)
    
    def upload_text_file(self, data:str, filename, _extension = "txt"):
        return self.upload_file(data.encode("utf-8"), filename)

    def get_file_info(self, ID:str):
        if not (self.get_file_exist(ID)):
            return None 
        
        _file = self.find_file(ObjectId(ID))

        _file_info = {
            "filename": _file.filename,
            "upload_timestamp": _file.T,
            #"upload_datetime": timestamp_to_datetime(_file.T),
            "extension": _file.E,
            "chunk_size": _file.chunk_size,
            "length": _file.length,
            #"size": bytes_to_Mb(_file.length),
            #"size_str": format_file_size_str(_file.length)
        }

        return _file_info

    
    def get_file_bytes(self, ID:str):
        return self.grid_fs.get(ObjectId(ID)).read()

    def get_file(self, ID:str):
        return self.grid_fs.get(ObjectId(ID))
    
    def get_file_exist(self, ID:str):
        return self.grid_fs.exists(ObjectId(ID))
    
    def delete_file(self, ID:str):
        return self.grid_fs.delete(ObjectId(ID))
    
    def download_file(self, ID:str, path):
        _bytes = self.get_file_bytes(ID)
        with open(path, "wb") as file:
            file.write(_bytes)
        return True
    
    #####################################################
    ##########      DATABASE BACKUP SYSTEM       ##########
    #####################################################
    
    # TODO:
    # La base de datos genérica no puede hacer una copia de seguridad de colecciones 
    # específicas debido a la presencia de tipos de datos no serializables o inconsistentes en objetos personalizados. 
    # Es necesario implementar una función personalizada de serialización para manejar estos objetos 
    # y asegurar una copia de seguridad adecuada.
    def BACKUP_ALL(self):
        _date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        
        
        for collection in self.database.list_collection_names():
            
            if (collection == "fs.chunks"):
                continue
            
            path = "BACKUPS/"+_date+"/"+collection
            create_dir(path)
            
            print("Creating Backup on > ", collection) 
            results = self.find({}, into=collection)
             
            for result in results:
                result["_id"] = str(result["_id"])
                
                with open(path + "/{}.BACKUP".format(result["_id"]), "w") as file:
                    json_data = json.dumps(result, default=custom_encoder)
                    file.write(json_data)
        
class DatabaseHelper():
    
    def get_database(name, collection = None, develop = False) -> Database:
        name = f'{name}_develop' if develop else name
        if (collection == None):
            return Database.databases[name]
        return Database.databases[name][collection]