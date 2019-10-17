class Possession():
    def __init__(self,players,time,score):
        '''
        :param players: A player list contains all in-court players
        :param time: Current time of the game (in seconds). The maximum time (without overtime periods) is 4*12*60 = 2880 seconds.
        :param score: The current score in a list. For instance {'Lakers' : 80, 'Spurs' : 90}
        '''
        self.players = players
        self.current_time = time
        self.score = score
        self.clutch = False        # follow the nba standard


    def identify_clutch(self,time,score):
        '''
        Identify if the current possession is within the clutch time. Return true if it is.
        :param time:
        :param score:
        :return:
        '''
        # This function should return True or False
        teams = self.score.keys()
        score_diff = abs(self.score[teams[0]]-self.score[teams[1]])
        if (time%720>420 and int(time/720) == 3 and score_diff <= 5) or (time%720>690 and int(time/720)<3):
            self.clutch = True #last five minutes, team score diff within 5, or last 30 seconds in each quarter
        else:
            self.clutch = False


    def handle_possession(self,players,time):
        pass