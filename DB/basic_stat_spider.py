# -*- coding: utf-8 -*-

# A special thanks to /b1llyh0yle who shares his free nba api online: https://www.balldontlie.io/#get-all-players
# I'm using this API to get the basic stats

import urllib.request
import urllib.parse
import json

def get_all_teams():
    url = "https://www.balldontlie.io/api/v1/teams"
    f = urllib.request.urlopen(url)
    content = f.read().decode('utf-8')
    return content

def