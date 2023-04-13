import sys

from config import settings
from mongo import MongoSingle, MongoCluster

if __name__ == '__main__':
    sys.stdout.write('Single mongo instance:\n')
    mongo_single = MongoSingle()

    for recs_num in [100, 1000, 10000, 100000]:
        for batch_size in [10, 100, 1000]:
            settings.batch_size = batch_size
            settings.recs_num = recs_num
            sys.stdout.write(f'\ndocs count: {settings.recs_num}, batch size: {settings.batch_size}\n')
            mongo_single.bulk_insert()
            mongo_single.bulk_unordered_insert()
            mongo_single.bulk_write_concern(1)
            mongo_single.bulk_insert_without_flush()
            mongo_single.read_all()
            mongo_single.bulk_insert_without_flush()
            mongo_single.get_avg_score()

    sys.stdout.write('\nMongo cluster:\n')
    mongo_replicaset = MongoCluster()

    for recs_num in [100, 1000, 10000, 100000]:
        for batch_size in [10, 100, 1000]:
            settings.batch_size = batch_size
            settings.recs_num = recs_num
            sys.stdout.write(f'\ndocs count: {settings.recs_num}, batch size: {settings.batch_size}\n')
            mongo_single.bulk_insert()
            mongo_single.bulk_unordered_insert()
            mongo_single.bulk_write_concern(1)
            mongo_single.bulk_insert_without_flush()
            mongo_single.read_all()
            mongo_single.bulk_insert_without_flush()
            mongo_single.get_avg_score()
