from hodolbot.bot import HodolBot


def main():
    with open("./token.txt", "r", encoding="utf-8") as f:
        token = f.readline()  # token 유출 방지

    client = HodolBot()
    client.run(token)
