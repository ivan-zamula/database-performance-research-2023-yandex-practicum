from pymongo import MongoClient, WriteConcern
from pymongo.errors import BulkWriteError

from config import settings
from utils import benchmark, get_test_data


class Mongo:

    def __init__(self):
        self.client = self.connect()
        self.db = self.client.get_database('someDb')
        self.collection = self.db.get_collection('someCollection')

    def connect(self):
        raise NotImplementedError

    @staticmethod
    def clear_db(func):
        def wrapper(self, *args, **kwargs):
            func(self, *args, **kwargs)
            self.collection.drop()
            self.client.admin.command({'planCacheClear': self.collection.name})
        return wrapper

    def bulk_insert_without_flush(self):
        for test_data in get_test_data():
            self.collection.insert_many(test_data)

    @clear_db
    @benchmark
    def bulk_insert(self):
        for test_data in get_test_data():
            self.collection.insert_many(test_data)

    @clear_db
    @benchmark
    def bulk_unordered_insert(self):
        for test_data in get_test_data(concern_data=True):
            self.collection.bulk_write(test_data, ordered=False)

    @clear_db
    @benchmark
    def read_all(self):
        self.collection.find({}, batch_size=settings.batch_size)

    @clear_db
    @benchmark
    def get_avg_score(self):
        self.collection.aggregate([{
            "$group": {
                "_id": None,
                "avg_$score": {"$avg": "$score"}
            }
        }])

    @clear_db
    @benchmark
    def bulk_write_concern(self, w: int):
        collection = self.db.get_collection(
            self.collection.name, write_concern=WriteConcern(w=w, wtimeout=1))
        try:
            for test_data in get_test_data(concern_data=True):
                collection.bulk_write(test_data)
        except BulkWriteError:
            pass


class MongoSingle(Mongo):

    def connect(self):
        return MongoClient(**settings.mongo_single.dict())


class MongoCluster(Mongo):

    def connect(self):
        return MongoClient(**settings.mongo_cluster.dict())
