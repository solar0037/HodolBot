import random
from discord import Message, TextChannel, VoiceChannel, Member, Embed, VoiceClient
from discord.ext.commands import Bot

from .stock import get_stock
from .covid19 import get_covid19
from .ranking import get_programming, get_anime


bot_name = "호돌봇"  # 봇 이름
bot_call = "!"  # 봇 호출


# 로그인
async def on_ready_fn(client: Bot):
    line = '-'*15
    username = client.user.name
    userid = client.user.id
    assert username == bot_name

    print(f"{line}\nLogged in as:\n{username}\n{userid}\n{line}")


# 메세지 처리
async def on_message_fn(client: Bot, message: Message):
    author: Member = message.author
    content: str = message.content
    channel: TextChannel = message.channel
    voice: VoiceClient = message.author.voice

    if content.startswith(bot_call):
        text = content.replace(bot_call, "").strip()  # "!"를 제외한 나머지 텍스트
        # print(f"message: {message}")
        print(f"message: {text}")

        # 안녕
        if text == '안녕':
            await channel.send(f"<@{author.id}> 어흥~!")

            voice_channel: VoiceChannel = voice.channel
            client.voice_client = await voice_channel.connect()

        # 잘가
        elif text == '잘가':
            await channel.send(f"<@{author.id}> ㅃ2")

            voice_client: VoiceClient = client.voice_client
            await voice_client.disconnect()

        # 말해
        elif text == '말해':
            await channel.send("안녕!")

        # 읊어
        elif text == '읊어':
            await channel.send("어흥 어흥 어흥")

        # 글써
        elif text == '글써':
            await channel.send("나랏말싸미...")

        # 주사위
        elif text == '주사위':
            num = random.randint(1, 6)
            await channel.send(f'주사위를 굴려 나온 숫자: {num}')

        # 주식
        elif text == '주식':
            stock = get_stock()
            await channel.send(stock)

        # 코로나
        elif text == '코로나':
            covid19 = get_covid19()
            await channel.send(covid19)

        # 프로그래밍
        elif text == '프로그래밍':
            programming = get_programming()
            await channel.send(programming)

        # 애니
        elif text == '애니':
            anime = get_anime()
            await channel.send(anime)

        # 개발자
        elif text == '개발자':
            url = {
                'dimipedia': 'https://dimipedia.net/wiki/%EC%82%AC%ED%98%B8%EC%A4%80',
                'github': 'https://github.com/sqrtpi177',
                'blog': 'https://blog.naver.com/moy0037',
                'facebook': 'https://www.facebook.com/profile.php?id=100029757106182',
                'youtube': "https://www.youtube.com/channel/UCkxI0ozgMOV3Akpyr6QQ5RQ"
            }
            title = '개발자 정보'
            description = 'AI입니다. 하지만 할 수 있는 게 아무것도 없습니다.\n궁금하면 찾아가 보시죠?'
            color = 0x0f4c81

            embed = Embed(title=title,
                          description=description,
                          color=color)
            embed.add_field(name='디미백과', value=url['dimipedia'], inline=False)
            embed.add_field(name='깃허브', value=url['github'], inline=False)
            embed.add_field(name='블로그', value=url['blog'], inline=False)
            embed.add_field(name='페이스북', value=url['facebook'], inline=False)
            embed.add_field(name="유튜브", value=url['youtube'], inline=False)
            await channel.send(embed=embed)

        # 도움
        elif text == '도움':
            help_list = "```nim\n" \
                        "!안녕: 만남 인사\n" \
                        "!잘가: 작별 인사\n" \
                        "!말해: 말하기\n" \
                        "!읊어: 시 읊기\n" \
                        "!글써: 글 쓰기\n" \
                        "!코로나: 코로나19 현황\n" \
                        "!주식: 코스피, 코스닥 현황\n" \
                        "!프로그래밍: 프로그래밍 언어 순위\n" \
                        "!애니: ㄴㄷㅆ\n" \
                        "!개발자: '그'의 정보"\
                        "```"

            await channel.send(help_list)
