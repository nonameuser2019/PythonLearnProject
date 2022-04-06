import json
with open('data.json', 'r') as f:
    reader = f.read()
    dict_data = json.loads(reader)['users']
    for row in dict_data:
        print(row)


cars = ['audi', 'mazda', 'vw']


