import os
import json


def init(message):
    with open('./data/gamble-data.json', 'w') as file:
        data = {message.author.id: '10000'}
        json.dump(data, file)


def wallet(message):
    script_dir = os.path.dirname(__file__)
    rel_path = 'data/gamble-data.json'
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, 'r') as file:
        json_data = json.load(file)
        return json_data[str(message.author.id)]
