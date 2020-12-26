from discord import TextChannel, Member
from discord.ext.commands import Bot

from hodolbot.functions import greetings_fn, views_fn, info_fn
from hodolbot.constants import BOT_CALL, LINE


class HodolBot(Bot):
    def __init__(self):
        super().__init__(command_prefix=BOT_CALL)

    async def on_ready(self) -> None:
        print(f"{LINE}\n" \
              f"Logged in as:\n" \
              f"{self.user.name}\n" \
              f"{self.user.id}\n" \
              f"{LINE}")

    async def on_message(self, message) -> None:
        author: Member = message.author
        content: str = message.content
        channel: TextChannel = message.channel

        if content.startswith(BOT_CALL):
            # ![명령어] -> [명령어]
            text = content.replace(BOT_CALL, "").strip()
            print(f"message: {text}")

            await greetings_fn(channel, author, text)
            await views_fn(channel, text)
            await info_fn(channel, text)
