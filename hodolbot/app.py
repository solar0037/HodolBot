import random

from discord import Message, TextChannel, Member, Embed
from discord.ext.commands import Bot

from hodolbot.views import views


bot_name = "호돌봇"  # 봇 이름
bot_call = "!"  # 봇 호출

def main():
    with open('./token.txt', 'r', encoding='utf-8') as f:
        token = f.readline()  # token 유출 방지

    client = HodolBot()
    client.run(token)


class HodolBot(Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    async def on_ready(self):
        line = '-'*15
        username = self.user.name
        userid = self.user.id
        print(f"{line}\nLogged in as:\n{username}\n{userid}\n{line}")

    async def on_message(self, message):
        author: Member = message.author
        content: str = message.content
        channel: TextChannel = message.channel

        if content.startswith(bot_call):
            text = content.replace(bot_call, "").strip()  # "!"를 제외한 나머지 텍스트
            print(f"message: {text}")

            for view in views:
                if text == view.command:
                    await channel.send(view.get())
                    break

            # 안녕
            if text == '안녕':
                await channel.send(f"<@{author.id}> 어흥~!")

            # 잘가
            elif text == '잘가':
                await channel.send(f"<@{author.id}> ㅃ2")

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
