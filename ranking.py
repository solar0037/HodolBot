from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import discord


class Ranking:
    def __init__(self, channel):  # set channel=None for debugging
        self.channel = channel
        self.message = ""
        self.embed = discord.Embed()

    def programming(self):
        url = "https://www.tiobe.com/tiobe-index/"
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"id": "top20"})
        tr_list = table.find("tbody").find_all("tr")

        lang_list = []
        for i in range(0, len(tr_list)):
            lang_list.append(tr_list[i].find_all("td")[3].text)

        for i, data in enumerate(lang_list):
            self.message += "{}위: {}\n".format(i + 1, data)

        # set message
        self.embed = discord.Embed(title='프로그래밍 언어 순위',
                                   color=0x0f4c81)
        self.embed.add_field(name="2020년 프로그래밍 언어 순위입니다.",
                             value='---------------------------------------------\n'
                                   + self.message
                                   + '---------------------------------------------',
                             inline=False)
        self.embed.set_footer(text='정보 제공: TIOBE')

    def anime(self):
        url = "http://anime.onnada.com/rank.php"
        html = requests.get(url)

        soup = BeautifulSoup(html.content.decode('utf-8', 'replace'), 'html.parser')
        tables = soup.find_all('table', class_='web-array')
        tr_list = tables[0].find_all('tr')
        # range(4, 23, 2)
        td_list = []
        for i in range(3, 23, 2):
            td_list.append(tr_list[i])
        anime_list = []
        for item in td_list:
            anime_list.append(item.find_all('td')[2].find('a').text)

        for i, data in enumerate(anime_list):
            self.message += "{}위: {}\n".format(i + 1, data)

        # set message
        self.embed = discord.Embed(title='애니메이션 순위',
                                   color=0x0f4c81)
        self.embed.add_field(name="애니메이션 순위입니다.",
                             value='---------------------------------------------\n'
                                   + self.message
                                   + '---------------------------------------------',
                             inline=False)
        self.embed.set_footer(text='정보 제공: 온나다')

    async def show(self, message):
        await self.channel.send(message, embed=self.embed)

    def debug(self):
        print(self.message)


if __name__ == '__main__':
    ranking = Ranking(None)
    ranking.programming()
    ranking.debug()

    ranking = Ranking(None)
    ranking.anime()
    ranking.debug()
