from bson import Int64, Decimal128, ObjectId
from bson.json_util import dumps

import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.people import People
from pymongo import MongoClient
from datetime import datetime

p = People()

d = p.collection.find_one()

print(d)
print(type(d))

j = dumps(d)
print(j)
print(type(j))

typified = {
    "_id": ObjectId("000000000000000000000001"),
    "an_int32": int(123),
    "an_int64": (pow(2, 33)),
    "a_float": float(123.456),
    "a_decimal128": Decimal128("3.141569"),
    "time_now": datetime.utcnow()
}

print(typified)

p.collection.update({"_id": typified["_id"]}, typified, upsert=True)

returned = p.collection.find_one({"_id": typified["_id"]})

print(returned)

print(dumps(returned))

print('an_int32', type(returned["an_int32"]))
print('an_int64', type(returned["an_int64"]))

