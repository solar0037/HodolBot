import discord
import requests
from bs4 import BeautifulSoup


async def show_stock(channel, url_k, url_last):
    # KOSPI, KOSDAQ, KPI200

    req_k = requests.get(url_k)
    html_k = req_k.text
    bs_k = BeautifulSoup(html_k, 'html.parser')

    kospi_now_value = bs_k.find('span', {'id': 'KOSPI_now'}).text[:-1]
    kospi_change_raw = bs_k.find('span', {'id': 'KOSPI_change'}).text
    kospi_change_value = kospi_change_raw.split(' ')[0][1:]
    kospi_change_rate = kospi_change_raw.split(' ')[1][:-3]
    kospi_change_value = decorate(kospi_change_value, kospi_change_rate)

    kosdaq_now_value = bs_k.find('span', {'id': 'KOSDAQ_now'}).text[:-1]
    kosdaq_change_raw = bs_k.find('span', {'id': 'KOSDAQ_change'}).text
    kosdaq_change_value = kosdaq_change_raw.split(' ')[0][1:]
    kosdaq_change_rate = kosdaq_change_raw.split(' ')[1][:-3]
    kosdaq_change_value = decorate(kosdaq_change_value, kosdaq_change_rate)

    kpi200_now_value = bs_k.find('span', {'id': 'KPI200_now'}).text[:-1]
    kpi200_change_raw = bs_k.find('span', {'id': 'KPI200_change'}).text
    kpi200_change_value = kpi200_change_raw.split(' ')[0][1:]
    kpi200_change_rate = kpi200_change_raw.split(' ')[1][:-3]
    kpi200_change_value = decorate(kpi200_change_value, kpi200_change_rate)

    # Top Stocks

    req_last = requests.get(url_last)
    html_last = req_last.text
    bs_last = BeautifulSoup(html_last, 'html.parser')

    last_name = []
    last_now_value = []
    last_change_value = []
    last_change_rate = []
    for i in range(2, 7):
        last = bs_last.find('table', {'class': 'type_5'}).find_all('tr')[i].find_all('td')
        last_name.append(last[1].text)
        last_now_value.append(last[3].text)
        last_change_value.append(last[4].find('span').text[5:-5])
        last_change_rate.append(last[5].find('span').text[5:])
        last_change_value[i-2] = decorate(last_change_value[i-2], last_change_rate[i-2])

    embed = discord.Embed(title='주식 정보', description='주식 정보입니다.', color=0x0f4c81)

    embed.add_field(name='------------------------------------------------------------',
                    value='[코스피, 코스닥, 코스피 200]',
                    inline=False)

    embed.add_field(name='코스피',
                    value=kospi_now_value + '\n' + kospi_change_value + ' ' + kospi_change_rate,
                    inline=True)
    embed.add_field(name='코스닥',
                    value=kosdaq_now_value + '\n' + kosdaq_change_value + ' ' + kosdaq_change_rate,
                    inline=True)
    embed.add_field(name='코스피 200',
                    value=kpi200_now_value + '\n' + kpi200_change_value + ' ' + kpi200_change_rate,
                    inline=True)

    embed.add_field(name='------------------------------------------------------------',
                    value='[검색상위 종목]',
                    inline=False)

    for i in range(0, 5):
        embed.add_field(name=last_name[i],
                        value=last_now_value[i] + '\n' + last_change_value[i] + ' ' + last_change_rate[i],
                        inline=True)

    embed.set_footer(text='정보 제공: 네이버 금융')

    await channel.send(embed=embed)


def decorate(value, rate):
    if rate[0] == '+':
        value = '▲'+value
    elif rate[0] == '-':
        value = '▼'+value
    else:
        value = '-'+value
    return value
