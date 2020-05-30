"""
Discord Experiments.
Updated whenever the author wants.
For experimenting things in discord.
"""

import discord
import calc
from stock import show_stock
from gamble import init, wallet

client = discord.Client()

bot_name = '호돌봇'  # bot name
bot_call = '호돌아'  # call bot

game_list = ['주사위 굴리기', '가위바위보', '로렘 입숨 생성기', '초성게임', '거꾸로 치기']  # 게임 이름


# log-in
@client.event
async def on_ready():
    print("------")
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("------")


# process message
@client.event
async def on_message(message):
    msg = message.content
    chnl = message.channel

    if msg.startswith(bot_call):

        # say hello
        if msg[4:6] == '안녕' \
                or msg[4:6] == '안뇽' \
                or msg[4:6] == '아령' \
                or msg[4:6] == '하이' \
                or msg[4:6] == 'ㅎㅇ':
            await chnl.send("어흥~!")

        # say goodbye
        elif msg[4:6] == '잘가' \
                or msg[4:6] == '꺼져' \
                or msg[4:6] == 'ㅃ2' \
                or msg[4:6] == 'ㅂ2' \
                or msg[4:6] == '빠이' \
                or msg[4:6] == '바이' \
                or msg[4:7] == '잘 가':
            await chnl.send("안 된다 이 악마야!")

        # stock
        elif msg[4:6] == '주식':
            url_k = "https://finance.naver.com/sise/"
            url_last = "https://finance.naver.com/sise/lastsearch2.nhn"
            await show_stock(chnl, url_k, url_last)

        # calculate
        elif msg[4:6] == '계산':
            if msg[7:11] == '원의둘레':
                await chnl.send(calc.circle_circumference(float(msg[12:])))
            elif msg[7:11] == '원의넓이':
                await chnl.send(calc.circle_area(float(msg[12:])))
            elif msg[7:10] == '방정식':
                code = calc.prob_to_code(msg)

                url = 'https://www.wolframalpha.com/input/?i='
                url += code
                await chnl.send(url)

        # play
        elif msg[4:7] == '놀아줘':
            if msg[8:11] == '말해봐' \
                    or msg[8:12] == '말해 봐':
                await chnl.send('안녕!')
            elif msg[8:11] == '읊어봐' \
                    or msg[8:12] == '읊어 봐':
                await chnl.send("어흥 어흥 어흥")
            elif msg[8:12] == '글 써봐' \
                    or msg[8:11] == '글써봐' \
                    or msg[8:13] == '글 써 봐':
                await chnl.send('나랏말싸미...')

        # learn
        elif msg[4:6] == '학습':
            await chnl.send("기능구현 예정")

        # gamble
        elif msg[4:6] == '도박':
            if msg[7:10] == '초기화':
                init(message)
                await chnl.send("@"+'555720974398652436'+"돈이 10000원으로 초기화됐습니다.")
            elif msg[7:9] == '지갑':
                money = wallet(message)
                await chnl.send("%d원 남았습니다." % int(money))
            elif msg[7:9] == '배팅':
                await chnl.send("")

        # ask for help
        elif msg[4:6] == '도움' \
                or msg[4:7] == '도움말' \
                or msg[4:7] == '도와줘':
            embed = discord.Embed(title='봇 정보',
                                  description="<명령어 목록>"
                                              "\n[안녕]"
                                              "\n[잘가]"
                                              "\n[계산]: 원의둘레, 원의넓이"
                                              "\n[주식]"
                                              "\n[놀아줘]: 말해봐, 읊어봐, 글 써봐"
                                              "\n[도박]: 초기화, 지갑, 베팅"
                                              "\n기타: [도움], [개발자]",
                                  color=0x0f4c81)
            await chnl.send(embed=embed)

        elif msg[4:7] == '개발자':
            embed = discord.Embed(title='개발자 정보',
                                  description="AI입니다. 하지만 할 수 있는 게 아무것도 없습니다.",
                                  color=0x0f4c81)
            embed.add_field(name='디미백과',
                            value='https://dimipedia.net/wiki/%EC%82%AC%ED%98%B8%EC%A4%80',
                            inline=False)
            embed.add_field(name='깃허브',
                            value='https://github.com/sqrtpi177',
                            inline=False)
            embed.add_field(name='블로그',
                            value='https://blog.naver.com/moy0037',
                            inline=False)
            await chnl.send(embed=embed)


# replace it with your token
client.run('token')
