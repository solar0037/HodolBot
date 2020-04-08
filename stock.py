import json
import requests
from bs4 import BeautifulSoup


async def make_file(json_url, json_file):
    url = json_url
    resp = requests.get(url)
    html = BeautifulSoup(resp.content, 'html.parser')
    text = html.get_text()
    file = open(json_file, 'w')
    file.write(text[30:-1])
    file.close()


async def print_stock(channel, json_file):
    with open(json_file) as file:
        json_data = json.load(file)
        nv = json_data['result']['areas'][0].get('datas')[0].get('nv')
        await channel.send("{}".format(nv))
        cv = json_data['result']['areas'][0].get('datas')[0].get('cv')
        cr = json_data['result']['areas'][0].get('datas')[0].get('cr')
        if cv > 0:
            await channel.send("▲{} +{}%".format(cv, cr))
        elif cv < 0:
            await channel.send("▼{} -{}%".format(abs(cr), abs(cr)))
        else:
            await channel.send("-0 0%")
