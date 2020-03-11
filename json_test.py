import json

with open('3.json', 'r', encoding='utf8')as fp:
    json_data = json.load(fp)
    for item in json_data:
        print(item['name'])
        if('deadCount' in item):
            print(item['deadCount'])
        else:
            continue

