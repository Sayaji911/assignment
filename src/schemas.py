from pydantic import BaseModel
from datetime import date, time



class BaseCountry(BaseModel):

    country_name: str

    class Config:
        orm_mode = True


class CreateCountry(BaseCountry):
    pass


class UpdateCountry(BaseCountry):
    pass


class Country(BaseCountry):
    id: int


class BaseMatch(BaseModel):
    match_date: date
    venue_id: int
    tournament_id: int

    class Config:
        orm_mode = True


class CreateMatch(BaseMatch):
    pass


class UpdateMatch(BaseMatch):
    pass


class Match(BaseMatch):
    id: int



class BaseMatchResult(BaseModel):

    match_result: str

    class Config:
        orm_mode = True


class CreateMatchResult(BaseMatchResult):
    pass


class UpdateMatchResult(BaseMatchResult):
    pass


class MatchResult(BaseMatchResult):
    id: int




class BaseMatchSummary(BaseModel):
    team_1_id: int
    team_2_id: int
    captain_player_1_id: int
    captain_player_2_id: int
    man_of_match_player_id: int
    bowler_of_match_player_id: int
    winner_team_id: int
    loser_team_id: int
    team_1_score: int
    team_2_score: int
    team_1_wicket: int
    team_2_wicket: int
    first_inning_team_id: int
    match_result_type_id: int
    match_id: int

    class Config:
        orm_mode = True


class CreateMatchSummary(BaseMatchSummary):
    pass


class UpdateMatchSummary(BaseMatchSummary):
    pass


class MatchSummary(BaseMatchSummary):
    id: int



class BaseMatchType(BaseModel):

    match_type: str

    class Config:
        orm_mode = True


class CreateMatchType(BaseMatchType):
    pass


class UpdateMatchType(BaseMatchType):
    pass


class MatchType(BaseMatchType):
    id: int

    class Config:
        orm_mode = True



class BasePlayer(BaseModel):
    name: str
    age: int
    dob: date
    retirement_date: date
    player_role_id: int
    team_id: int

    class Config:
        orm_mode = True

class CreatePlayer(BasePlayer):
    pass


class UpdatePlayer(BasePlayer):
    pass


class Player(BasePlayer):
    id: int



class BasePlayerBatProfile(BaseModel):
    matches: int
    innings: int
    no_of_not_outs: int
    runs: int
    highest_score: int
    average: int
    no_of_balls_faced: int
    strike_rate: int
    half_centuries: int
    full_centuries: int
    boundaries: int
    sixes: int
    player_id: int

    class Config:
        orm_mode = True

class CreatePlayerBatProfile(BasePlayerBatProfile):
    pass

class UpdatePlayerBatProfile(BasePlayerBatProfile):
    pass


class PlayerBatProfile(BasePlayerBatProfile):
    id: int



class BasePlayerBowlProfile(BaseModel):
    matches: int
    innings: int
    no_of_deliveries: int
    runs: int
    wickets: int
    best_bowling_in_match: int
    economy: str
    average: str
    player_id: int

    class Config:
        orm_mode = True

class CreatePlayerBowlProfile(BasePlayerBowlProfile):
    pass


class UpdatePlayerBowlProfile(BasePlayerBowlProfile):
    pass


class PlayerBowlProfile(BasePlayerBowlProfile):
    id: int


class BasePlayerRole(BaseModel):

    role_name: str

    class Config:
        orm_mode = True


class CreatePlayerRole(BasePlayerRole):
    pass


class UpdatePlayerRole(BasePlayerRole):
    pass


class PlayerRole(BasePlayerRole):
    id: int






class BaseTeam(BaseModel):
    # team_name: Optional[str] = None

    team_name: str
    country_id: int

    class Config:
        orm_mode = True


class CreateTeam(BaseTeam):
    pass


class UpdateTeam(BaseTeam):
    pass


class Team(BaseTeam):
    id: int

    class Config:
        orm_mode = True



class BaseTeamProfile(BaseModel):
    total_wins: int
    total_loses: int
    no_of_matches: int
    rank: int
    team_id: int

    class Config:
        orm_mode = True

class CreateTeamProfile(BaseTeamProfile):
    pass


class UpdateTeamProfile(BaseTeamProfile):
    pass


class TeamProfile(BaseTeamProfile):
    id: int


class BaseTournament(BaseModel):
    name: str
    first_place_team_id: int
    second_place_team_id: int
    third_place_team_id: int
    start_date: date
    end_date: date
    total_points: int
    team_id: int

    class Config:
        orm_mode = True

class CreateTournament(BaseTournament):
    pass

class UpdateTournament(BaseTournament):
    pass

class Tournament(BaseTournament):
    id: int



class BaseVenue(BaseModel):
    venue_name: str
    venue_location: str

    class Config:
        orm_mode = True

class CreateVenue(BaseVenue):
    pass

class UpdateVenue(BaseVenue):
    pass

class Venue(BaseVenue):
    id: int






