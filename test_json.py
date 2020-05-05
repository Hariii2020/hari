import json

json_data='{"a":1,"b":2,"c":3,"d":4,"e":5}'

parsed_json=(json.loads(json_data))
print(json.dumps(parsed_json,indent=4,sort_keys=True))

loaded_json=json.loads(json_data)
for x in loaded_json:
    print("%s: %d"%(x,loaded_json))

class Test(object):
    def __init__(self,data):
        self.__dict__=json.loads(data)

test1=Test(json_data)
print(test1.a)

with open('details.json','r')as f:
    detais_dict=json.load(f)

for detail in detais_dict:
    print(detail['Name'])





