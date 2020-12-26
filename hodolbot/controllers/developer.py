from discord import Embed
from hodolbot.models import DeveloperModel


def developer_handler() -> Embed:
    data =  DeveloperModel.get()

    embed = Embed(title="개발자 정보",
                  description=\
                    "AI입니다. 하지만 할 수 있는 게 아무것도 없습니다.\n" \
                    "궁금하면 찾아가 보시죠?",
                  color=0x0f4c81)
    embed.add_field(name="디미백과", value=data["dimipedia"], inline=False)
    embed.add_field(name="깃허브", value=data["github"], inline=False)
    embed.add_field(name="블로그", value=data["blog"], inline=False)
    embed.add_field(name="페이스북", value=data["facebook"], inline=False)
    embed.add_field(name="유튜브", value=data["youtube"], inline=False)

    return embed
