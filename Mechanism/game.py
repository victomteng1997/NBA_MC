from Element.player import Player
from Element.team import Team

class Possession():
    def __init__(self,home_team_players,visit_team_players,time,score):
        '''
        :param players: A player list contains all in-court players
        :param time: Current time of the game (in seconds). The maximum time (without overtime periods) is 4*12*60 = 2880 seconds.
        :param score: The current score in a list. For instance {'Lakers' : 80, 'Spurs' : 90}
        '''
        self.players = players
        self.current_time = time
        self.score = score
        self.clutch = False        # follow the nba standard


    def identify_clutch(self):
        '''
        Identify if the current possession is within the clutch time. Return true if it is.
        :return:
        '''
        # This function should return True or False
        time = self.current_time
        score = self.score
        teams = self.score.keys()
        score_diff = abs(self.score[teams[0]]-self.score[teams[1]])
        if (time%720>420 and int(time/720) == 3 and score_diff <= 5) or (time%720>690 and int(time/720)<3):
            self.clutch = True #last five minutes, team score diff within 5, or last 30 seconds in each quarter
        else:
            self.clutch = False


    def handle_possession(self,players,time):
        self.identify_clutch()
        pass

class Game():
    def __init__(self, home_team, visit_team):
        self.home_team = home_team
        self.visit_team = visit_team
        self.current_time = 0
        self.current_score = {"home":0, "visit":0}
        self.home_team_players = self.home_team.players
        self.visit_team_players = self.visit_team.players


    def handle_posession(self):

        # initiate a new possession
        new_possession = Possession(self.home_team_players,self.visit_team_players,self.current_time,self.current_score)
