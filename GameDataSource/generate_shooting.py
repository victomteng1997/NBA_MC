import json
import os
import pprint

# we use the legend Vince Carter as an example
def readwrite_shooting_stats(split,filename):
    f = open('..\\DB\\2018-19\\generalsplits\\' + str(filename), 'r')
    content = f.readlines()
    f.close()
    stats_dict = json.loads(content[0])
    player_stats = {}
    # Now let's focus on shooting.
    # field goal
    focused_headers = ['FGA','FGM','FG3A','FG3M','FG_PCT','FC3_PCT','FTA','FTM','MIN']
    try:
        for i in range(0,len(stats_dict['resultSets'][0]['headers'])):
            if stats_dict['resultSets'][0]['headers'][i] in focused_headers:
                player_stats[stats_dict['resultSets'][0]['headers'][i]] = stats_dict['resultSets'][0]['rowSet'][0][i]
    except: # Most likely no data, give zero
        for i in range(0,len(stats_dict['resultSets'][0]['headers'])):
            if stats_dict['resultSets'][0]['headers'][i] in focused_headers:
                player_stats[stats_dict['resultSets'][0]['headers'][i]] = 0


    directory = 'players\\2018-19\\'+str(filename)+'\\shooting'
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(directory+'\\general.txt', 'w') as f:
        json.dump(player_stats,f)


all_names = os.listdir("..\\DB\\2018-19\\generalsplits\\")
print(all_names)
for name in all_names:
    # print(name)
    readwrite_shooting_stats('shootingsplits',name)