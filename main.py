"""
Discord Experiments.
Updated whenever the author wants.
For experimenting things in discord.
"""

import discord
import stock
import ranking

client = discord.Client()

bot_name = "호돌봇"  # bot name
bot_call = "호돌아"  # bot call


# log in
@client.event
async def on_ready():
    print("---------------")
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")


# handle messages
@client.event
async def on_message(message):
    content: str = message.content
    channel = message.channel

    if content.startswith(bot_call):
        text = content.replace(bot_call, "").strip()  # text excluding "호돌아 "

        # ##################################################
        # commands for playing
        for s in ['안녕', '안뇽', '아령', '하이', 'ㅎㅇ']:
            if s in text:
                await channel.send("어흥~!")
                break

        for s in ['잘가' '잘 가', '꺼져', 'ㄲㅈ', 'ㅃ2', '빠이', '바이']:
            if s in text:
                await channel.send("안 된다 이 악마야!")
                break

        for s in ['말해봐', '말해 봐', '말해']:
            if s in text:
                await channel.send("안녕!")
                break
        for s in ['읊어봐', '읊어 봐', '읊어']:
            if s in text:
                await channel.send("어흥 어흥 어흥")
                break
        for s in ['글써봐', '글써 봐', '글 써봐', '글 써 봐']:
            if s in text:
                await channel.send("나랏말싸미...")
                break

        # ##################################################
        # commands for information
        if '주식' in text:
            # check if it's help command
            is_help = 0
            for h in ['도움', '도움말', '도와줘']:
                if h in text:
                    is_help = 1
            if is_help:
                pass

            else:
                if '주요종목' in text:
                    stk = stock.Stock(channel)
                    stk.all_major()
                else:
                    stk = stock.Stock(channel)
                await stk.show()

        for s in ['순위', '랭킹']:
            if s in text:
                # check if it's help command
                is_help = 0
                for h in ['도움', '도움말', '도와줘']:
                    if h in text:
                        is_help = 1
                if is_help:
                    pass

                else:
                    if '프로그래밍' in text:
                        url = "https://www.tiobe.com/tiobe-index/"
                        rank = ranking.Ranking(channel)
                        rank.programming(url)
                        await rank.show("")
                        break

        # ##################################################
        # commands for misc
        for s in ['도움', '도움말', '도와줘']:
            if s in text:
                if '인사' in text:
                    embed = discord.Embed(title="인사",
                                          description="호돌봇이 당신에게 인사합니다!"
                                                      "\n[안녕]: 만남 인사"
                                                      "\n[잘가]: 작별 인사",
                                          color=0x04fc81)
                elif '놀기' in text:
                    embed = discord.Embed(title="놀기",
                                          description="호돌봇이 당신과 놀아줍니다!"
                                                      "\n재미 없을 지도 몰라요."
                                                      "\n[말해봐]: 말하기"
                                                      "\n[읊어봐]: 시 읊기"
                                                      "\n[글 써봐]: 글 쓰기",
                                          color=0x04fc81)
                elif '주식' in text:
                    embed = discord.Embed(title="주식",
                                          description="주식 현황을 알려줍니다."
                                                      "\n아직은 코스피, 코스닥, 코스피200밖에 없어요."
                                                      "\n[주식]: 주식 데이터",
                                          color=0x04fc81)
                elif '순위' in text:
                    embed = discord.Embed(title="순위",
                                          description="각종 순위를 보여줍니다."
                                                      "\n별 신기한 게 다 있어요!"
                                                      "\n[순위]-[프로그래밍]: 프로그래밍 언어 순위",
                                          color=0x04fc81)
                elif '개발자' in text:
                    embed = discord.Embed(title="개발자",
                                          description="저를 창조한 분이에요!"
                                                      "\n[개발자]: '그'의 정보 확인하기",
                                          color=0x04fc81)
                else:
                    embed = discord.Embed(title='봇 정보',
                                          description="",
                                          color=0x04fc81)
                    embed.add_field(name='명령어 목록',
                                    value="\n인사: [안녕], [잘가]"
                                          "\n놀기: [말해봐], [읊어봐], [글 써봐]"
                                          "\n주식: [주식]"
                                          "\n순위: [순위]-[프로그래밍]"
                                          "\n기타: [도움], [개발자]",
                                    inline=False)
                await channel.send(embed=embed)
                break

        if '개발자' in text:
            # check if it's help command
            is_help = 0
            for h in ['도움', '도움말', '도와줘']:
                if h in text:
                    is_help = 1
            if is_help:
                pass

            else:
                embed = discord.Embed(title='개발자 정보',
                                      description="AI입니다. 하지만 할 수 있는 게 아무것도 없습니다."
                                                  "\n궁금하면 찾아가 보시죠?",
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
                embed.add_field(name='페이스북',
                                value='https://www.facebook.com/profile.php?id=100029757106182',
                                inline=False)
                embed.add_field(name="유튜브",
                                value="https://www.youtube.com/channel/UCkxI0ozgMOV3Akpyr6QQ5RQ",
                                inline=False)
                await channel.send(embed=embed)


if __name__ == '__main__':
    # replace it with your token
    client.run('token')
