from discord.ext.commands import Bot
from app import on_ready_fn, on_message_fn


class HodolBot(Bot):
    def __init__(self):
        super().__init__(command_prefix='!')

    async def on_ready(self):
        await on_ready_fn(self)

    async def on_message(self, message):
        await on_message_fn(client, message)


if __name__ == '__main__':
    with open('./token.txt', 'r', encoding='utf-8') as f:
        token = f.readline()  # token 유출 방지

    client = HodolBot()
    client.run(token)
