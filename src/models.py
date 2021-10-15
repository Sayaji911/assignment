from sqlalchemy import DateTime, Column, String, Integer, CheckConstraint, ForeignKey, DECIMAL
from database import time
from src.database import  Base
from typing import Optional
from sqlalchemy.orm import relationship

#Country model inheriting from Base class
#with tablename as country and rows as id and name
class Country(Base):
    __tablename__ = "Country"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)

#Teams model inheriting from Base class
#with tablename as Teams and rows as id and name
class Teams(Base):
    __tablename__ = "Teams"
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)


#Profile model inheriting from Base class
#with tablename as Profile and rows as id, name, matches_played, won and lost, and current postition
#also matches won and lost should always be less than total matches played
class Profile(Base):
    __tablename__ = 'Profile'
    id = Column(Integer,primary_key=True)
    matches_played = Column(Integer,nullable=False)
    matches_won = Column(Integer,nullable=False)
    matches_lost = Column(Integer,nullable=False)
    position = Column(Integer,nullable=False)
    __table_args__ = ( CheckConstraint(matches_won <= matches_played and
                                       matches_lost <= matches_played))
#Player model inheriting from Base class
#with tablename as Player and rows as id and name and
# team will be in referenced to primary key of teams table
class Player:
    __tablename__ = 'Player'

    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    team = Column(Integer,ForeignKey(Teams.id))
    age = Column(Integer,nullable=False)
    height = Column(DECIMAL,nullable=False)
    role_in_id = Column(Integer,nullable=False)
    dob = Column(DateTime,nullable=False)
    __tableargs__ = (CheckConstraint(age > 0 and height > 0))

class Matches(Base):
    __tablename__ = 'Matches'
    id = Column(Integer,primary_key=True)
    date = Column(DateTime,nullable=False)
    time = Column(time)
    venue = Column(Integer,nullable=False)



class Venue(Base):
    __tablename__  = 'Venue'
    id = Column(Integer,primary_key=True)
    stadium_name = Column(String(100),nullable=False)
    city = Column(String(100),nullable=False)


class MatchSummary(Base):
    __tablename__ = "MatchSummary"

    id = Column(Integer,primary_key=True)
    team_1 = Column(Integer)
    team_2 = Column(Integer)
    toss_winner_team = Column(Integer)
    first_innings_team = Column(Integer)
    second_innigs_team = Column(Integer)
    captain_team_1 = Column(Integer)
    captain_team_2 = Column(Integer)
    winner_team = Column(Integer)
    losing_team = Column(Integer)
    man_of_the_match = Column(Integer)
    bowler_of_the_match = Column(Integer)
    team_1_runs = Column(Integer)
    team_2_runs = Column(Integer)
    team_1_wickets = Column(Integer)
    team_2_wickets = Column(Integer)
    best_fielder = Column(Integer)







