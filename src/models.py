from sqlalchemy import DateTime, Column, String, Integer, CheckConstraint, ForeignKey, DECIMAL
from datetime import time
from src.database import Base
from sqlalchemy.orm import relationship


# Country model inheriting from Base class
# with tablename as country and rows as id and name
class Country(Base):
    __tablename__ = "Country"

    id = Column(Integer, primary_key=True)
    country_name = Column(String, nullable=True)

#Model Match having colomn
#tournament pointing to tournaments id
#column match_summary relationship with MatchSummary class
class Match(Base):
    __tablename__ = "Match"

    id = Column(Integer, primary_key=True)
    match_date = Column(DateTime, nullable=True)
    venue_id = Column(Integer)
    tournament_id = Column(Integer, ForeignKey('Tournament.id'))
    match_summary = relationship("MatchSummary")

class MatchResult(Base):
    __tablename__ = "MatchResult"

    id = Column(Integer, primary_key=True)
    match_result = Column(String, nullable=True)


class MatchSummary(Base):
    __tablename__ = "MatchSummary"

    id = Column(Integer, primary_key=True)
    team_1_id = Column(Integer)
    team_2_id = Column(Integer)
    captain_player_1_id = Column(Integer)
    captain_player_2_id = Column(Integer)
    man_of_match_player_id = Column(Integer)
    bowler_of_match_player_id = Column(Integer)
    winner_team_id = Column(Integer)
    loser_team_id = Column(Integer)
    team_1_score = Column(Integer)
    team_2_score = Column(Integer)
    team_1_wicket = Column(Integer)
    team_2_wicket = Column(Integer)
    first_inning_team_id = Column(Integer)
    match_result_type_id = Column(Integer)
    #players match id is pointed to class Match id
    match_id = Column(Integer, ForeignKey('Match.id'))



class MatchType(Base):
    __tablename__ = "MatchType"

    id = Column(Integer, primary_key=True)
    match_type = Column(String, nullable=True)
    
#class Player with coloumn team_id pointin to class Teams id
#column playerbat_profile, bowl_profile having many to many relationship with
#PlayerBatProfile and PlayerBowlProfile
class Player(Base):
    __tablename__ = "Player"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    dob = Column(DateTime, nullable=True)
    retirement_date = Column(DateTime, nullable=True)
    player_role_id = Column(Integer)
    team_id = Column(Integer, ForeignKey('Team.id'))
    player_bat_profile = relationship("PlayerBatProfile")
    player_bowl_profile = relationship("PlayerBowlProfile")


#Class PlayerBatProfile
#having coloumn player_id pointing to class Players id
class PlayerBatProfile(Base):
    __tablename__ = "PlayerBatProfile"

    id = Column(Integer, primary_key=True)
    matches = Column(Integer, nullable=True)
    innings = Column(Integer, nullable=True)
    no_of_not_outs = Column(Integer, nullable=True)
    runs = Column(Integer, nullable=True)
    highest_score = Column(Integer, nullable=True)
    average = Column(Integer, nullable=True)
    no_of_balls_faced = Column(Integer, nullable=True)
    strike_rate = Column(Integer, nullable=True)
    half_centuries = Column(Integer, nullable=True)
    full_centuries = Column(Integer, nullable=True)
    boundaries = Column(Integer, nullable=True)
    sixes = Column(Integer, nullable=True)
    player_id = Column(Integer, ForeignKey('Player.id'))

#Class PlayerBowlProfile
#having coloumn player_id pointing to class Players id
class PlayerBowlProfile(Base):
    __tablename__ = "PlayerBowlProfile"

    id = Column(Integer, primary_key=True)
    matches = Column(Integer, nullable=True)
    innings = Column(Integer, nullable=True)
    no_of_deliveries = Column(Integer, nullable=True)
    runs = Column(Integer, nullable=True)
    wickets = Column(Integer, nullable=True)
    best_bowling_in_match = Column(Integer, nullable=True)
    economy = Column(String, nullable=True)
    average = Column(Integer, nullable=True)
    SR = Column(String, nullable=True)
    W5 = Column(String, nullable=True)
    W10 = Column(String, nullable=True)
    player_id = Column(Integer, ForeignKey('Player.id'))



class PlayerRole(Base):
    __tablename__ = "PlayerRole"

    id = Column(Integer, primary_key=True)
    role_name = Column(String, nullable=True)


#class Team with column havig many to many relationship with Class TeamProfile
class Team(Base):
    __tablename__ = "Team"

    id = Column(Integer, primary_key=True)
    team_name = Column(String, nullable=True)
    country_id = Column(Integer)
    player = relationship("Player")
    team_profile = relationship("TeamProfile")

#this class has column team_id with points to Class Teams id.
class TeamProfile(Base):
    __tablename__ = "TeamProfile"

    id = Column(Integer, primary_key=True)
    total_wins = Column(Integer, nullable=True)
    total_loses = Column(Integer, nullable=True)
    no_of_matches = Column(Integer, nullable=True)
    rank = Column(Integer, nullable=True)
    team_id = Column(Integer, ForeignKey('Team.id'))

#class tournament having column match which points to Match class so it can show the specific matchs detail
class Tournament(Base):
    __tablename__ = "Tournament"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    first_place_team_id = Column(String, nullable=True)
    second_place_team_id = Column(String, nullable=True)
    third_place_team_id = Column(String, nullable=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    total_points = Column(Integer, nullable=True)
    team_id = Column(Integer)
    match = relationship("Match")

class Venue(Base):
    __tablename__ = "Venue"

    id = Column(Integer, primary_key=True)
    venue_name = Column(String, nullable=True)
    venue_location = Column(String, nullable=True)


