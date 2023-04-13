from pydantic import BaseSettings, Field, BaseModel


class MongocClusterSettings(BaseModel):
    host: str = 'mongos1'
    port: int = 27017


class MongoSingleSettings(BaseModel):
    host: str = 'single_mongo'
    port: int = 27017


class Settings(BaseSettings):
    mongo_single = MongoSingleSettings()
    mongo_cluster = MongocClusterSettings()
    recs_num: int = 10000
    batch_size: int = 100


settings = Settings()
