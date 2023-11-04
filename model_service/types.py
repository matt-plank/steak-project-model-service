from datetime import datetime
from typing import Literal, TypedDict

Doneness = Literal["raw", "rare", "medium", "well-done", "burnt"]


class Measurement(TypedDict):
    thickness: float
    cookTime: int
    doneness: Doneness


class Coefs(TypedDict):
    thickness: float
    bias: float


class Model(TypedDict):
    created: datetime
    doneness: Doneness
    coefficients: Coefs
