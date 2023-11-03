import os

from pymongo import MongoClient

from .types import Measurement

MONGO_URI: str = os.environ["MONGO_URI"]
MONGO_DATABASE: str = os.environ["MONGO_DATABASE"]


client = MongoClient(MONGO_URI)
database = client[MONGO_DATABASE]
measurements = database.measurements
models = database.models


def all_measurements() -> list[Measurement]:
    return list(measurements.find({}))
