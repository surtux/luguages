"""The purpose of this module is to test the database connection
"""


from unittest import TestCase
#from luguages.src import *
from pymongo import MongoClient

class TestConnection(TestCase):
    
    def test_db_connection(self):
        client = MongoClient('localhost',27017)
        db = client['items']
        collections = db.list_collection_names()
        self.assertIn('books',collections)

    def test_update(self):
        pass