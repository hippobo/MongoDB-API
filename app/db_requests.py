from app.database import DatabaseConnection
from bson.objectid import ObjectId

class DB_connection:
    def __init__(self, database_name, address : str = 'localhost', port : int = 27017):
        self.db = DatabaseConnection(database_name).get_database()

    def get_collection(self, collection_name):
        '''This method is to get a document from the database.'''
        a = self.db[collection_name]
        return a
    def get_document_by_id(self, collection_name, id ):
        id = ObjectId(id)
        a = self.db.get_collection(collection_name).find_one({"_id": id})
        a['_id'] = str(a['_id'])
        return a 
    def get_random_document(self, collection_name):
        a = self.db.get_collection(collection_name).aggregate([{"$sample": {"size": 1}}]).to_list(1)
        a = str(a)
        
        return a
    

