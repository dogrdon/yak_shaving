from pymongo import MongoClient
from config import Database as mDb

c = MongoClient()
db = c[mDb._dbName]
collection = db[mDb._collection]






