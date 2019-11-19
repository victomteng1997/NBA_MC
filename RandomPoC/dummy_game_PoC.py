from Mechanism.game import Game
from Element.team import Team

random_team_1 = Team()
random_team_2 = Team()

final_result = {}

for i in range(0,10000):
    my_dummy_game = Game(random_team_1, random_team_2)
    result = my_dummy_game.simulate_game()
    if result in final_result:
        final_result[result] += 1
    else:
        final_result[result] = 1
print(final_result)
