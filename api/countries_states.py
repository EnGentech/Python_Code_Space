from pprint import pprint
import json

with open("content.json", 'r', encoding='utf-8') as file:
    getme = json.load(file)

for x in getme:
    print(x['name']['common'], x['common_sub'])
