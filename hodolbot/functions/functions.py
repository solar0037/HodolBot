import random
from discord import TextChannel, Member
from hodolbot import views


async def greetings_fn(channel: TextChannel, author: Member, text: str) -> None:
    if text == "안녕":
        await channel.send(f"<@{author.id}> 어흥~!")

    # 잘가
    elif text == "잘가":
        await channel.send(f"<@{author.id}> ㅃ2")

    # 말해
    elif text == "말해":
        await channel.send("안녕!")

    # 읊어
    elif text == "읊어":
        await channel.send("어흥 어흥 어흥")

    # 글써
    elif text == "글써":
        await channel.send("나랏말싸미...")

    # 주사위
    elif text == "주사위":
        num = random.randint(1, 6)
        await channel.send(f"주사위를 굴려 나온 숫자: {num}")


async def views_fn(channel: TextChannel, text: str) -> None:
    for view in [views.Covid19View,
                 views.ProgrammingView,
                 views.AnimeView,
                 views.StockView]:
        if text == view.command:
            await channel.send(view.get())
            break


async def info_fn(channel: TextChannel, text: str) -> None:
    if text == views.DeveloperView.command:
        await channel.send(embed=views.DeveloperView.get())

    elif text == "도움":
        await channel.send(
            "```nim\n" \
            "!안녕: 만남 인사\n" \
            "!잘가: 작별 인사\n" \
            "!말해: 말하기\n" \
            "!읊어: 시 읊기\n" \
            "!글써: 글 쓰기\n" \
            "!코로나: 코로나19 현황\n" \
            "!주식: 코스피, 코스닥 현황\n" \
            "!프로그래밍: 프로그래밍 언어 순위\n" \
            "!애니: ㄴㄷㅆ\n" \
            "!개발자: \"그\"의 정보"\
            "```")
