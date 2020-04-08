"""
Discord Experiments.
Updated whenever the author wants.
For experimenting things in discord.
"""

import discord
import os
import calc
from stock import make_file, print_stock

client = discord.Client()


@client.event
async def on_ready():
    print("------")
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("------")


@client.event
async def on_message(message):
    msg = message.content
    chnl = message.channel

    if msg.startswith('!안녕'):
        await chnl.send('아령~!')

    elif msg.startswith('!잘가'):
        await chnl.send('ㅃ2')
        await client.logout()
        print('Logged out')
        print("------")

    elif msg.startswith('!도움'):
        await chnl.send('계산: 원의둘레, 원의넓이')
        await chnl.send('주식: 코스피, 코스닥')

    elif msg.startswith('!주식'):
        if msg[4:] == '코스피':
            url = 'https://polling.finance.naver.com/api/realtime.nhn?' \
                  '_callback=window.__jindo_callback._6352&query=SERVICE_INDEX%3AKOSPI'
            script_dir = os.path.dirname(__file__)
            rel_path = 'json/kospi.json'
            abs_file_path = os.path.join(script_dir, rel_path)
            await make_file(url, abs_file_path)
            await print_stock(chnl, abs_file_path)

        elif msg[4:] == '코스닥':
            url = 'https://polling.finance.naver.com/api/realtime.nhn?' \
                  '_callback=window.__jindo_callback._3106&query=SERVICE_INDEX%3AKOSDAQ'
            script_dir = os.path.dirname(__file__)
            rel_path = 'json/kosdaq.json'
            abs_file_path = os.path.join(script_dir, rel_path)
            await make_file(url, abs_file_path)
            await print_stock(chnl, abs_file_path)

    elif msg.startswith('!계산'):
        if '원의둘레' in msg:
            await chnl.send(calc.circle_circumference(float(msg[9:])))
        elif '원의넓이' in msg:
            await chnl.send(calc.circle_area(float(msg[9:])))

    elif msg.startswith('!학습'):
        await chnl.send("기능구현 예정")


# replace it with your token
client.run('token')
