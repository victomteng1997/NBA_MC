# -*- coding: utf-8 -*-

# For simplicity, I'm not using any beautifulsoup or webparser library. All handles are written by myself.
import urllib.request
import urllib.parse
import json

def get_string_between(line,start,end):
    s = line
    result = s[s.find(start)+len(start):s.rfind(end)]
    return result

def process_player_page(player_dictionary):
    ## Verify first
    players_stat = {}
    player_badges = {}
    print("Start player stat processing work. Total length: %s"%str(len(player_dictionary)))
    print('-----------------------------------------')
    for player in player_dictionary:
        print("Working on %s"%player)
        base_url = player_dictionary[player]
        f = urllib.request.urlopen(base_url)
        content = f.read().decode('utf-8')
        content = content.split('\n')
        player_stat = {}
        for i in range(0, len(content)):
            line = content[i]

            # get overall:
            if '<span class="attribute-box attribute-box-scale attribute-large overall amethyst" data-original-value=' in line:
                player_stat['overall'] = get_string_between(line, '">', '</span>')
            # get total:
            elif '<span class="attribute-box attribute-box-scale total" data-original-value="' in line:
                player_stat['total'] = get_string_between(line, 'data-original-value="', '" data')
            elif '<span class="attribute-boost evolution-boost"></span>' in line:
                if content[i - 1].split()[0] == '<strong>':
                    player_stat[line.split()[0]] = content[i - 2].split()[0]
                else:
                    player_stat[line.split()[0]] = content[i - 1].split()[0]
        for key in list(player_stat.keys()):
            if player_stat[key].isdigit() == False:
                del player_stat[key]
        players_stat[player] = player_stat
    return players_stat


def update_database():
    print("hi")
    player_pages = {}
    base_url = 'https://2kmtcentral.com/20/players/theme/current'

    # step 1: test for connection
    f = urllib.request.urlopen(base_url)
    content = f.read().decode('utf-8')
    if 'a class="name box-link" href="https://2kmtcentral.com/20/players' in content:
        print("Connected. Start crawling.")
        pass
    else:
        print("Connection failed. Job terminated.")
        return # terminate the process

    base_page_number = 0
    while True:
        # crawl on each page:
        print("Working on page number %s"%str(base_page_number))
        page_url = base_url + '/page/%s'%str(base_page_number)
        f = urllib.request.urlopen(page_url)
        content = f.read().decode('utf-8')
        if 'a class="name box-link" href="https://2kmtcentral.com/20/players' in content:
            parsed_content = content.split('\n')
            #print(len(parsed_content))
            for line in parsed_content:
                if 'a class="name box-link" href="https://2kmtcentral.com/20/players' in line:
                    player_name = get_string_between(line,'<strong>','</strong>')
                    player_page = get_string_between(line,'href="','">')
                    #print(player_name,player_page)
                    player_pages[player_name] = player_page
            base_page_number += 1
        else:
            print("Info gathering work finished.")
            print("Get %s number of players in total." %str(len(player_pages)))
            break # stop trying to request for pages

    players_stat = process_player_page(player_dictionary=player_pages)
    return players_stat




players_stat = update_database()
# writing everything into json and store in players_stat.json
print(players_stat.keys())
with open('2k_players_stat.json', 'w') as f:
    json.dump(players_stat, f)


###############################
# the following is a test
'''
url = 'https://2kmtcentral.com/20/players/2342/kawhi-leonard'
f = urllib.request.urlopen(url)
content = f.read().decode('utf-8')
content = content.split('\n')
player_stat = {}
for i in range(0,len(content)):
    line = content[i]

    # get overall:
    if '<span class="attribute-box attribute-box-scale attribute-large overall amethyst" data-original-value=' in line:
        player_stat['overall'] = get_string_between(line, '">','</span>')
    # get total:
    elif '<span class="attribute-box attribute-box-scale total" data-original-value="' in line:
        player_stat['total'] = get_string_between(line, 'data-original-value="','" data')
    elif '<span class="attribute-boost evolution-boost"></span>' in line:
        if content[i-1].split()[0] == '<strong>':
            player_stat[line.split()[0]] = content[i - 2].split()[0]
        else:
            player_stat[line.split()[0]] = content[i - 1].split()[0]
for key in list(player_stat.keys()):
    if player_stat[key].isdigit() == False:
        del player_stat[key]
print(player_stat)





'''