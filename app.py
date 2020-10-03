import random
import discord

from stock import Stock
from ranking import Ranking
from covid19 import Covid19


bot_name = "호돌봇"  # 봇 이름
bot_call = "호돌아"  # 봇 호출


# 로그인
async def on_ready_fn(client):
    print("---------------")
    print("Logged in as:")
    print(client.user.name)
    print(client.user.id)
    print("---------------")


# 메세지 처리
async def on_message_fn(message):
    content: str = message.content
    channel: discord.TextChannel = message.channel

    if content.startswith(bot_call):
        text = content.replace(bot_call, "").strip()  # "호돌아 "를 제외한 나머지 텍스트
        print(f"message: {text}")

        # default=True -> 축약 검사
        default = True

        ##################################################
        #                   인사, 놀기                   #
        ##################################################

        # 인사: 안녕
        for s in ['안녕', '안뇽', '아령', '하이', 'ㅎㅇ']:
            if s in text:
                await channel.send("어흥~!")
                default = False
                break

        # 인사: 잘가
        for s in ['잘가', '잘 가', '꺼져', 'ㄲㅈ', 'ㅃ2', '빠이', '바이']:
            if s in text:
                await channel.send("안 된다 이 악마야!")
                default = False
                break

        # 놀기: 말해봐
        for s in ['말해봐', '말해 봐', '말해']:
            if s in text:
                await channel.send("안녕!")
                default = False
                break

        # 놀기: 읊어봐
        for s in ['읊어봐', '읊어 봐', '읊어']:
            if s in text:
                await channel.send("어흥 어흥 어흥")
                default = False
                break

        # 놀기: 글 써봐
        for s in ['글써봐', '글써 봐', '글 써봐', '글 써 봐']:
            if s in text:
                await channel.send("나랏말싸미...")
                default = False
                break

        # 놀기: 주사위
        for s in ['주사위']:
            if s in text:
                num = random.randint(1, 6)
                await channel.send(f'주사위를 굴려 나온 숫자: {str(num)}')

        ##################################################
        #               주식, 코로나, 순위               #
        ##################################################

        # 주식: 주식
        for s in ['주식']:
            if s in text and not is_help(text):
                stock = Stock(channel)
                stock.all_major()
                await stock.show()
                default = False

        # 코로나: 코로나
        for s in ['코로나']:
            if s in text and not is_help(text):
                covid19 = Covid19(channel)
                covid19.all()
                await covid19.show()
                default = False

        # 순위: 순위
        for s in ['순위', '랭킹']:
            if s in text and not is_help(text):
                # 순위 - 프로그래밍
                for keyword in ['프로그래밍', '플밍']:
                    if keyword in text:
                        ranking = Ranking(channel)
                        ranking.programming()
                        await ranking.show()
                        default = False
                        break

                # 순위 - 애니
                for keyword in ['애니', '애니메이션', '아니메']:
                    if keyword in text:
                        ranking = Ranking(channel)
                        ranking.anime()
                        await ranking.show()
                        default = False
                        break

        ##################################################
        #                   개발자                       #
        ##################################################

        # 기타: 개발자
        for s in ['개발자', '만든 사람']:
            if s in text and not is_help(text):
                embed = discord.Embed(title='개발자 정보',
                                      description="AI입니다. 하지만 할 수 있는 게 아무것도 없습니다.\n"
                                                  "궁금하면 찾아가 보시죠?",
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

        ##################################################
        #               default: 축약 등 검사            #
        ##################################################

        # 주식
        if default and not is_help(text):
            # 순위 - 프로그래밍
            for keyword in ['프로그래밍', '플밍']:
                if keyword in text:
                    ranking = Ranking(channel)
                    ranking.programming()
                    await ranking.show()
                    break

            # 순위 - 애니메이션
            for keyword in ['애니', '애니메이션', '아니메']:
                if keyword in text:
                    ranking = Ranking(channel)
                    ranking.anime()
                    await ranking.show()
                    break

        ##################################################
        #                   도움말                       #
        ##################################################

        # 기타: 도움
        if is_help(text):
            for s in ['도움', '도움말', '도와줘']:
                if s in text:
                    if '인사' in text:
                        embed = discord.Embed(title="인사",
                                              description="호돌봇이 당신에게 인사합니다!\n"
                                                          "[안녕]: 만남 인사\n"
                                                          "[잘가]: 작별 인사",
                                              color=0x04fc81)
                    elif '놀기' in text:
                        embed = discord.Embed(title="놀기",
                                              description="호돌봇이 당신과 놀아줍니다!\n"
                                                          "재미 없을 지도 몰라요.\n"
                                                          "[말해봐]: 말하기\n"
                                                          "[읊어봐]: 시 읊기\n"
                                                          "[글 써봐]: 글 쓰기",
                                              color=0x04fc81)
                    elif '코로나' in text:
                        embed = discord.Embed(title="코로나",
                                              description="코로나19 현황을 알려줍니다.\n"
                                                          "[코로나]: 코로나19 현황",
                                              color=0x04fc81)
                    elif '주식' in text:
                        embed = discord.Embed(title="주식",
                                              description="주식 현황을 알려줍니다.\n"
                                                          "아직은 코스피, 코스닥, 코스피200밖에 없어요.\n"
                                                          "[주식]: 주식 데이터",
                                              color=0x04fc81)
                    elif '순위' in text:
                        embed = discord.Embed(title="순위",
                                              description="각종 순위를 보여줍니다.\n"
                                                          "별 신기한 게 다 있어요!\n"
                                                          "[순위]\n"
                                                          "-[프로그래밍]: 프로그래밍 언어 순위\n"
                                                          "-[애니]: ㄴㄷㅆ",
                                              color=0x04fc81)
                    elif '개발자' in text:
                        embed = discord.Embed(title="개발자",
                                              description="저를 창조한 분이에요!\n"
                                                          "[개발자]: '그'의 정보 확인하기",
                                              color=0x04fc81)
                    else:
                        embed = discord.Embed(title='봇 정보',
                                              description="",
                                              color=0x04fc81)
                        embed.add_field(name='명령어 목록',
                                        value="\n인사: [안녕], [잘가]"
                                              "\n놀기: [말해봐], [읊어봐], [글 써봐], [주사위]"
                                              "\n주식: [주식]"
                                              "\n코로나: [코로나]"
                                              "\n순위: [순위]-[프로그래밍], [애니]"
                                              "\n기타: [도움], [개발자]",
                                        inline=False)
                    await channel.send(embed=embed)
                    break


# 도움말인지 검사
def is_help(text):
    for h in ['도움', '도움말', '도와줘']:
        if h in text:
            return True
