import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from util.people import People
from pymongo import MongoClient

p = People()

doc = {"name": "kim", "age": 23}

p.collection.insert_one(doc)

docs = [{"name": "ogg", "age": 24}, {"name": "sal", "age": 25}]

p.collection.insert_many(docs)

for person in p.collection.find():
    print('---------')
    print(person)

p.collection.insert_one
