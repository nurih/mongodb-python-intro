from pymongo import MongoClient
from datetime import datetime

DB_CONNECTION = "mongodb://localhost/"

DB_NAME = "pyintro"

client = MongoClient("mongodb://localhost")

db = client[DB_NAME]
dir(db)

peeps = db.peeps
# ^^ same as db.get_collection('peeps')

person_1 = {"name": "bob", "likes": ["toast", "butter"], "date": datetime.utcnow()}


person_id = peeps.insert_one(person_1).inserted_id

print(person_id)

print(person_1)

# no filter
found = peeps.find_one()

print("no filter:", found)

# filter by id
found = peeps.find_one({"_id": person_id})

print("found with id:",found)

# filter by id - when inserted, the id was populated behind the scenes.
found = peeps.find_one({"_id": person_1["_id"]})

print("found with document's id field:",found)

print("Id can be any type. this one is", type(found["_id"]))

count = peeps.count_documents({})

print(f'* {count} documents found in ')

list = peeps.find({"name": "bob"})

for doc in list:
    print(f'* This {doc["name"]} has id {doc["_id"]}')
