import requests
from bs4 import BeautifulSoup

from hodolbot.classes import Model
from hodolbot.types import ProgrammingData, AnimeData


class ProgrammingModel(Model):
    url = 'https://www.tiobe.com/tiobe-index/'
    
    @classmethod
    def get(cls) -> ProgrammingData:
        html = requests.get(cls.url)
        soup = BeautifulSoup(html.text, 'html.parser')
        table = soup.find('table', {'id': 'top20'})
        tr_list = table.find('tbody').find_all('tr')

        return [
            tr_list[i].find_all('td')[3].text
            for i in range(len(tr_list))
        ]


class AnimeModel(Model):
    url = 'http://anime.onnada.com/rank.php'

    @classmethod
    def get(cls) -> AnimeData:
        html = requests.get(cls.url, verify=False)
        soup = BeautifulSoup(html.content.decode('utf-8', 'replace'), 'html.parser')

        tables = soup.find_all('table', class_='web-array')
        tr_list = tables[0].find_all('tr')
        td_list = []
        for i in range(3, 43, 2):
            td_list.append(tr_list[i])

        return [
            item.find_all('td')[2].find('a').text
            for item in td_list
        ]
