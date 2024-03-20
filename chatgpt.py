import openai
import json

with open('myapikey', 'r', encoding='utf') as key:
    API_KEY = key.read()
openai.api_key = API_KEY
try:
    with open('responseGPT.json', 'r', encoding='utf-8') as response:
        obtained = json.load(response)
except Exception:
    obtained = {}
foundValue = 0

def load_data():
    respond = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'user', 'content': assistance}
        ])
    store = respond['choices'][0]['message']['content']
    print(store)
    obtained[assistance] = store
    with open('responseGPT.json', 'w', encoding='utf-8') as save:
        json.dump(obtained, save)

while True:
    assistance = input('Ask me anything$ ')
    if obtained:
        for question, values in obtained.items():
            if assistance in question:
                foundValue = 1
                print(obtained[assistance])
                break
    else:
        load_data()
    if foundValue == 0:
        load_data()
