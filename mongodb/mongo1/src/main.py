import sys

from mongo import MongoSingle, MongoReplicaSet

if __name__ == '__main__':
    sys.stdout.write('Single mongo instance:\n')
    mongo_single = MongoSingle()

    mongo_single.bulk_insert()
    mongo_single.bulk_unordered_insert()
    mongo_single.bulk_write_concern(1)

    mongo_single.bulk_insert_without_flush()
    mongo_single.read_all()
    sys.stdout.write('Mongo replica set:\n')
    mongo_replicaset = MongoReplicaSet()

    mongo_replicaset.bulk_insert()
    mongo_replicaset.bulk_unordered_insert()
    mongo_replicaset.bulk_write_concern(3)

    mongo_replicaset.bulk_insert_without_flush()
    mongo_replicaset.read_all()
