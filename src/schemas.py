from typing import List, Optional
from pydantic import BaseModel
from datetime import date, time


class BaseCountry(BaseModel):
    name = str


class Country(BaseCountry):
    class Config():
        orm_mode = True


class ShowCountry(BaseCountry):
    name = str

    class Config():
        orm_mode = True


class BasePlayer(BaseModel):
    name = str
    team = int
    age = int
    height = int
    role_in_id = int
    dob = date


class Player(BasePlayer):
    class Config():
        orm_mode = True


class ShowPlayer(BaseModel):
    name = str
    team = int
    age = int
    height = int
    role_in_id = int
    dob = date

    class Config():
        orm_mode = True


class BaseMatch(BaseModel):
    date = date
    time = time
    venue = int


class Match(BaseMatch):
    class Config():
        orm_mode = True


class ShowMatch(BaseModel):
    date = date
    time = time
    venue = int

    class Config():
        orm_mode = True


