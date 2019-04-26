from pymongo import MongoClient
from datetime import datetime

DB_CONNECTION = 'mongodb://localhost/'

DB_NAME = 'pyintro'

client = MongoClient('mongodb://localhost')

db = client[DB_NAME]
dir(db)

peeps = db.peeps

person_1 = {
    'name': 'bob',
    'likes': ['toast', 'butter'],
    'date': datetime.utcnow(),
}


person_id = peeps.insert_one(person_1).inserted_id

print(person_id)

print(person_1)

print(peeps.find_one())






