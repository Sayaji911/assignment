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
    type = str

    class Config():
        orm_mode = True


class BaseResult(BaseModel):
    result = str


class Result(BaseResult):
    class Config():
        orm_mode = True


class ShowResult(BaseModel):
    class Config():
        orm_mode = True


class BaseMatchSummary(BaseModel):
    id = int
    team_1 = int
    team_2 = int
    toss_winner_team = int
    first_innings_team = int
    second_innings_team = int
    captain_team_1 = int
    captain_team_2 = int
    winner_team = int
    losing_team = int
    man_of_the_match = int
    bowler_of_the_match = int
    team_1_runs = int
    team_2_runs = int
    team_1_wickets = int
    team_2_wickets = int
    best_fielder = int


class MatchSummary(BaseMatchSummary):
    class Config():
        orm_mode = True


class ShowMatchSummary(BaseModel):
    class Config():
        orm_mode = True

class BaseVenue(BaseModel):
    stadium_name = str
    city = str

class Venue(BaseVenue):
    class Config():
        orm_mode = True

class ShowVenue(BaseModel):
    stadium_name = str
    city = str

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
    class Config():
        orm_mode = True

class BaseBattingProfile(BaseModel):
    Player_id = int
    _runs = int
    current_runs = int
    matches_played = int
    sixers = int
    fours = int
    full_centuries = int
    half_centuries = int

class BattingProfile(BaseBattingProfile)
     class Config():
         orm_mode = True

class ShowBattingProfile(BaseModel):
    Player_id = int
    _runs = int
    current_runs = int
    matches_played = int
    sixers = int
    fours = int
    full_centuries = int
    half_centuries = int

    class Config():
        orm_mode = True


class BaseBallingProfile(BaseModel):
    Player_id = int
    matches_played = int
    wickets = int
    deliveries = int

class BallingProfile(BaseBallingProfile):
    class Config():
        orm_mode = True

class ShowBallingProfie(BaseModel):
    Player_id = int
    matches_played = int
    wickets = int
    deliveries = int

