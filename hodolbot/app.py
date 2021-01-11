from hodolbot.bot import HodolBot
from hodolbot.utils import get_env


def main():
    token = get_env("BOT_TOKEN")
    # with open("./token.txt", "r", encoding="utf-8") as f:
    #     token = f.readline()  # token 유출 방지

    client = HodolBot()
    client.run(token)
