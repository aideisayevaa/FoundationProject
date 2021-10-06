#json-javascript object notation

import json

with open('data.json','r') as f:
    content = json.load(f) #json faylinin daxilindeki datani alsin
    print(content)
    print(type(content)) #cavab dict cixir
    print(type(content['friends'])) #cavab list
    print(type(content['friends'][0]))
    