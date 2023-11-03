import os

from pymongo import MongoClient

MONGO_URI: str = os.environ["MONGO_URI"]
MONGO_DATABASE: str = os.environ["MONGO_DATABASE"]


client = MongoClient(MONGO_URI)
database = client[MONGO_DATABASE]
measurements = database.measurements
models = database.models


def all_measurements():
    return measurements.find({})
