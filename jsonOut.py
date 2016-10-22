import json
import os
from pprint import pprint

data = {'Monday':
            {930: 70,
             830: 0,
             1800:70,
             100:0},
        'Tuesday':
            {930: 660,
             830: 0,
             1800:70,
             100:0}
        }

with open('./json/data.json', 'w') as outfile:
    json.dump(data, outfile)

pprint(data)