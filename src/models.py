from sqlalchemy import DateTime, Column, String, Integer, CheckConstraint, ForeignKey
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
    id = Column(Integer,primary_key=True)
    name = Column(String(100),nullable=False)
    team = Column(Integer,ForeignKey(Teams.id))
    age = Column(Integer,nullable=False)

