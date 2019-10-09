
class Player():
    def __init__(self,name):
        self.name = name

class Team():
    def __init__(self,name):
        '''
        Initialization of the Team class. The following attributes are initialized in this function
        team.name: Name of the team. Default = N.A.
        team.players: Players in the team, which is a list object that contains player instance (under Player class). Empty list in default.
        team.salary_cap: Salary cap, for further development. Default = 0
        '''
        self.name = "N.A."
        self.players = []
        self.salary_cap = 0

    def addPlayer(self, player_to_add):
        '''
        Add player into <team.players>.
        return the current number of players.
        :param player_to_add:
        :return: True
        '''
        self.players.append(player_to_add)
        return True

    def removePlayer(self,player_to_remove):
        '''
        Remove players from the current team.
        :param player_to_remove:
        :return remove_status: True when player removed successful, False when unsuccessful
        '''
        try:
            self.players.remove(player_to_remove)
        except:
            return False
        finally:
            return True

lebron = Player('lebron')
team = Team('team1')

team.addPlayer(lebron)
print(team.players)
team.addPlayer(lebron)
print(team.players)
team.removePlayer('lebron')
print(team.players)
team.removePlayer(lebron)
print(team.players)


