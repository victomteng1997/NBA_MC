# -*- coding: utf-8 -*-

class Team():
    def __init__(self):
        '''
        Initialization of the Team class. The following attributes are initialized in this function
        team.name: Name of the team. Default = N.A.
        team.players: Players in the team, which is a list object that contains player instance (under Player class). Empty list in default.
        team.salary_cap: Salary cap, for further development. Default = 0
        '''
        self.name = "N.A."
        self.players = []
        self.salary_cap = 0

    def searchPlayer(self,player_name):
        '''
        Search players within a team based on given player name
        :param player_name: The name of the player to search
        :return: list of player objects that fulfills the search requirement
        '''
        player_list = []
        for player in self.players:
            if player_name.lower() in player.name.lower():  # A basic, brief search that ignores upper case chars.
                player_list.append(player)
        return player_list

    def addPlayer(self, player_to_add):
        '''
        Add player into <team.players>.
        return the current number of players.
        :param player_to_add:
        :return: True
        '''
        self.players.append(player_to_add)
        return True

    def removePlayer(self, player_to_remove):
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

    def displayAllPlayersNames(self):
        '''
        Return names of players in the team
        :return player_name_list: A list that contains names of all players within the team
        '''
        players_name_list = []
        for player in self.players:
            players_name_list.append(player.name)
        return players_name_list



