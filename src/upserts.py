import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from lib.people import People
from pymongo import MongoClient

p = People()

match = {"name": "qui"}
update = {"$inc": {"age": 1}}


op_result = p.collection.update_one(match, update, upsert=True)

print(
    "matched",
    op_result.matched_count,
    "modified",
    op_result.modified_count,
    "upserted",
    op_result.upserted_id,
)

print(p.collection.find_one({"name": "qui"}))

op_result = p.collection.update_one(match, update, upsert=True)

print(
    "matched",
    op_result.matched_count,
    "modified",
    op_result.modified_count,
    "upserted",
    op_result.upserted_id,
)

print(p.collection.find_one({"name": "qui"}))
