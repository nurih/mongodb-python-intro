import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from util.people import People
from pymongo import MongoClient

p = People()

match = {"age": {"$lte": 25}}
update = {"$inc": {"age": 1}}


op_result = p.collection.update_many(match, update)
print('matched', op_result.matched_count, 'modified', op_result.modified_count, 'upserted')


for person in p.collection.find({}, {"_id": 0, "age": 1, "name": 1}):
    print("---------")
    print(person)
