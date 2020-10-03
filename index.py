"""
호돌봇의 소스코드입니다.
깃허브 레포지토리: https://github.com/sqrtpi177/hodol-bot
"""

import discord
from app import on_ready_fn, on_message_fn

client = discord.Client()


# 로그인
@client.event
async def on_ready():
    await on_ready_fn(client)


# 메세지 처리
@client.event
async def on_message(message):
    await on_message_fn(message)


if __name__ == '__main__':
    with open('./token.txt', 'r', encoding='utf-8') as f:
        token = f.readline()  # token 유출 방지
    client.run(token)
