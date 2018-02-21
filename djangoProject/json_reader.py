import json

json_data = open('data.json')   
data1 = json.load(json_data) 
print(data1)

json_data.close()