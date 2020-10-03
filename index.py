"""
호돌봇의 소스코드입니다.
깃허브 레포지토리: https://github.com/sqrtpi177/hodol-bot
"""

import discord
from app import on_ready_fn, on_message_fn


class BotClient(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        await on_ready_fn(client)

    async def on_message(self, message):
        await on_message_fn(message)


if __name__ == '__main__':
    with open('./token.txt', 'r', encoding='utf-8') as f:
        token = f.readline()  # token 유출 방지

    client = BotClient()
    client.run(token)
