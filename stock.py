import discord
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Stock:
    def __init__(self, channel):
        self.channel = channel
        self.stocks = []

    # add all major stocks(kospi, kosdaq, kospi200)
    def all_major(self):
        self.stock_major('kospi')
        self.stock_major('kosdaq')
        self.stock_major('kospi200')

    # add major stock(kospi, kosdaq, kospi200)
    def stock_major(self, stock_type):
        eng2kor = {'kospi': '코스피', 'kosdaq': '코스닥', 'kospi200': '코스피200'}

        url = "https://finance.naver.com/sise/sise_index.nhn?code=" + stock_type.upper()
        req = urllib.request.Request(url)
        html = urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        nv = soup.find("em", {"id": "now_value"}).text.strip()
        c_raw = soup.find("span", {"id": "change_value_and_rate"}).text.strip()
        cv = c_raw.split(' ')[0]
        cr = c_raw.split(' ')[1]
        cv, cr = decorate(cv, cr)
        self.stocks.append({'name': eng2kor[stock_type],
                            'nv': nv,
                            'cv': cv,
                            'cr': cr})

    # show stock
    async def show(self):
        embed = discord.Embed(title='주식 정보',
                              description='코스피, 코스닥, 코스피200 정보입니다.',
                              color=0x0f4c81)

        for data in self.stocks:
            embed.add_field(name=data['name'],
                            value="{}\n{} {}".format(data['nv'], data['cv'], data['cr']),
                            inline=True)

        embed.set_footer(text='정보 제공: 네이버 금융')

        await self.channel.send(embed=embed)


def decorate(value, rate: str):
    if rate[0] == '+':
        value = '▲'+value
        rate = rate.replace("상승", "")
    elif rate[0] == '-':
        value = '▼'+value
        rate = rate.replace("하락", "")
    else:
        value = '-'+value
    return value, rate
