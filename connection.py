from pymongo import MongoClient
from config import Database as db

c = MongoClient()
db = c[db._NAME]
collection = db[db._COLLECTION]






