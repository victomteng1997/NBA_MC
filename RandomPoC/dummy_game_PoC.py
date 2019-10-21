from Mechanism.game import Game
from Element.team import Team

random_team_1 = Team()
random_team_2 = Team()

my_dummy_game = Game(random_team_1, random_team_2)
while my_dummy_game.game_end == False:
    my_dummy_game.jump_ball()
    my_dummy_game.do_one_possession()