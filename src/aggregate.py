from pymongo import MongoClient
from datetime import datetime
from bson.son import SON
import pprint

DB_CONNECTION = "mongodb://localhost/"

DB_NAME = "pyintro"

client = MongoClient("mongodb://localhost")

db = client[DB_NAME]
dir(db)

peeps = db.peeps
# ^^ same as db.get_collection('peeps')

# count documents by name.
match = {"$match": {"name": {"$exists": True, "$ne": "voldermort"}}}
groupby = {"$group": {"_id": "$name", "count": {"$sum": 1}}}
project = {"$project": {"name": "$_id", "count": True, "_id": False}}
sortby = {"$sort": SON([("count", -1), ("name", 1)])}
found = peeps.aggregate([match, groupby, project, sortby])

print("Name Frequency")
print("==============")
pprint.pprint(list(found))
