from pymongo import MongoClient


class People():
    DB_NAME = 'pyintro'
    COLLECTION_NAME = 'peeps'

    def __init__(self, url = 'mongodb://localhost'):
        self.url = url
        self.client = MongoClient(url)
        self.db = self.client.get_database(self.DB_NAME)
        self.collection = self.db[People.COLLECTION_NAME]


