from bs4 import BeautifulSoup
from urllib.request import urlopen
import discord


class Ranking:
    def __init__(self, channel):
        self.channel = channel
        self.embed = discord.Embed()

    def programming(self, url):
        html = urlopen(url)
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find("table", {"id": "top20"})
        tr_list = table.find("tbody").find_all("tr")

        lang_list = []
        for i in range(0, len(tr_list)):
            lang_list.append(tr_list[i].find_all("td")[3].text)

        message = ""
        for i, data in enumerate(lang_list):
            message += "{}위: {}\n".format(i + 1, data)
        self.embed = discord.Embed(title='프로그래밍 언어 순위',
                                   color=0x0f4c81)
        self.embed.add_field(name="2020년 프로그래밍 언어 순위입니다.",
                             value='---------------------------------------------\n'
                                   + message
                                   + '---------------------------------------------',
                             inline=False)
        self.embed.set_footer(text='정보 제공: TIOBE')

    async def show(self, message):
        await self.channel.send(message, embed=self.embed)
