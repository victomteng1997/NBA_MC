import random

from Element.player import Player
from Element.team import Team

class Possession():
    def __init__(self,home_team_players,visit_team_players,time,score,possession_owner):
        '''
        :param home_team_players: player elements in a list for home team
        :param visit_team_players: player elements in a list for visit team
        :param time: Current time of the game (in seconds). The maximum time (without overtime periods) is 4*12*60 = 2880 seconds.
        :param score: The current score in a list. For instance {'Lakers' : 80, 'Spurs' : 90}
        '''
        self.possession_owner = possession_owner  #"home" or "visit"
        self.home_team_players  = home_team_players
        self.visit_team_players = visit_team_players
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

    def random_case_generator(self, case_list):
        '''
        :param case_list: The case list should be a list like this: ['case0':0.1,'case1':0.2, ...]
        Take note that for the above scenario, the probability for both case 1 and case 2 are 10%. (I believe you get it)
        :return: the index of the case selected by the random generator.
        '''
        # check valid or not first
        random_int = random.randint(0, 1000)
        for i in range(0,len(case_list)):
            if case_list[i][1] > 1:
                print("error in case probability. Check machanism\game.py")
            if random_int < case_list[i][1]*1000.0:
                return i
            else:
                pass
        return i + 1


    def handle_possession(self):
        self.identify_clutch()
        pass

    def handle_possession_for_testing(self):
        # Do an intialization
        score = 0
        change_possession = True
        # Work based on 2019/10/21 ideas
        # We just create a random mapping table:
        naive_possession_table = [('steal:',0.01),('def_rebound',0.4),('off_rebound',0.5),('1_points',0.6),('2_pints',0.83),
                                  ('3_points',0.9),('4_points',0.91),('foul_keep_pos',0.95),('foul_change_pos',1.0)]
        result = self.random_case_generator(naive_possession_table)
        # I'm too lazy to use a case for this dummy one:
        if result == 0 or result == 8 or result == 1:
            change_possession = True
            score = 0
        elif result == 2 or result == 7:
            change_possession = False
            score = 0
        elif result == 3:
            change_possession = True
            score = 1
        elif result == 4:
            change_possession = True
            score = 2
        elif result == 5:
            change_possession = True
            score = 3
        elif result == 6:
            change_possession = True
            score = 4
        time = min(random.randint(5,24),(720-self.current_time%720))
        return change_possession, score, time


class Game():
    def __init__(self, home_team, visit_team):

        # game attribute
        self.home_team = home_team
        self.visit_team = visit_team
        self.current_time = 0
        self.current_score = {"home":0, "visit":0}
        self.home_team_players = self.home_team.players
        self.visit_team_players = self.visit_team.players
        self.possession_owner = None
        self.on_court_home_players = []
        self.on_court_visit_players = []
        self.in_game_stats = {}
        self.game_end = False

        # game setting
        self.print_game_details = False


    def jump_ball(self):
        # a naive jumpball, half half prob
        teams = ['home','visit']
        self.possession_owner = teams[random.randint(0, 1)]

    def check_leader(self):
        '''
        Get the leader in the current game.
        Utilize the inbuilt self.score
        :return: leading team
        '''
        leading_team = max(self.current_score, key=self.current_score.get)
        return leading_team

    def do_one_possession(self):
        # initiate a new possession
        new_possession = Possession(self.home_team_players,self.visit_team_players,self.current_time,self.current_score,self.possession_owner)
        ############# ALERT, the following line is only for testing purpose.
        change_possession, score, time = new_possession.handle_possession_for_testing()
        self.current_score[self.possession_owner] += score
        if score != 0 and self.print_game_details:
            print(str(self.possession_owner) + "scored " + str(score))
        self.current_time += time
        if change_possession:
            if self.possession_owner == 'home':
                self.possession_owner = 'visit'
            else:
                self.possession_owner = 'home'

        if self.print_game_details:
            print('Current time: ', self.current_time, " Current_score: ",self.current_score)

        if self.current_time >= 12*60*4:
            self.game_end = True

    def simulate_game(self):
        '''
        Simulate the game with do_one_possession function
        :return: winner of the game
        '''
        self.jump_ball()
        while not self.game_end:
            self.do_one_possession()
        game_winner = self.check_leader()
        print("Game winner: ", game_winner)
        return game_winner
