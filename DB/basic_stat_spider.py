# -*- coding: utf-8 -*-

# The script downloads data from stats.nba.com through github project https://github.com/seemethere/nba_py.


import urllib.request
import urllib.parse
import json
import pandas

from nba_py import player
from nba_py import game
from nba_py.constants import *
import urllib.request
from requests import get
from nba_py.player import get_player

# headers={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Encoding":"gzip, deflate"}

def get_player_names(season):
    json = player.PlayerList(season = season).json
    return json

result = get_player_names('2018-19')
print(result)
my_own_namelist = {}
for i in result['resultSets'][0]['rowSet']:
    my_own_namelist[i[2]] = [i[0]]

for name in my_own_namelist.keys():
    player_id = my_own_namelist[name]
    print(name,player_id)
    season = '2018-19'
    stats = player.PlayerGeneralSplits(player_id=player_id,season=season).json
    #print(json.dumps(stats,indent=4,sort_keys=True))
    # So for now I don't care about the parameters in the dictionary. I just save them down first.
    target_dir = str(season)+'\\'+str(player_id)+'_'+str(name)
    with open(target_dir, 'w') as f:
        json.dump(stats, f)
