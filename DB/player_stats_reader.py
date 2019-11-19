import json
import pprint

# we use the legend Vince Carter as an example
def read_stats(split):
    f = open('2018-19\\'+str(split)+'\\[1713]_Vince Carter', 'r')
    content = f.readlines()
    f.close()


    stats_dict = json.loads(content[0])
    # pprint.pprint(stats_dict)
    # Here is the overall structure for the json
    #for i in range(0,len(stats_dict['resultSets'][0]['headers'])):
    #    print(stats_dict['resultSets'][0]['headers'][i], ' : ', stats_dict['resultSets'][0]['rowSet'][0][i])


read_stats('shootingsplits')