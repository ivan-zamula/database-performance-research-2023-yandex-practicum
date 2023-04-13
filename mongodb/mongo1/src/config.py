from pydantic import BaseSettings, Field, BaseModel


class MongoSingleSettings(BaseModel):
    host: str = 'single_mongo'
    port: int = 27017


class MongoReplicaSettings(BaseModel):
    id: int = Field(alias='_id')
    host: str


class MongoReplicaSetSettings(BaseModel):
    id: str = Field('myReplicaSet', alias='_id')
    members: list[MongoReplicaSettings] = [
        MongoReplicaSettings(_id=0, host='mongo1:27017'),
        MongoReplicaSettings(_id=1, host='mongo2:27017'),
    ]


class Settings(BaseSettings):
    mongo_single = MongoSingleSettings()
    mongo_replicaset = MongoReplicaSetSettings()
    recs_num: int = 10000000
    batch_size: int = 100000


settings = Settings()
