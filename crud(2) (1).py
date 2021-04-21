from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:33796' % ("admin", "test"))
        self.database = self.client['project']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    def read(self, query):
        data = ""
        if data is not None:
            data = self.database.animals.find(query, {"_id": False})
        else:
            data = self.database.animals.find( {}, {"_id": False})
        return data
    
    def delete(self, query):
        if query is not None:
            self.database.animals.delete_one(query)
        
    def update(self, query, newValue):
        self.database.animals.update_one(query,newValue)
        