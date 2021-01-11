from discord import TextChannel, Member
from discord.ext.commands import Bot

from hodolbot.functions import greetings_fn, views_fn, info_fn
from hodolbot.utils.get_env import get_env
from hodolbot.constants import LINE, DEVELOPMENT_BOT_CALL, PRODUCTION_BOT_CALL


class HodolBot(Bot):
    def __init__(self):
        if int(get_env("PRODUCTION", 0)):
            self.BOT_CALL = PRODUCTION_BOT_CALL
        else:
            self.BOT_CALL = DEVELOPMENT_BOT_CALL
        super().__init__(command_prefix=self.BOT_CALL)

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

        if content.startswith(self.BOT_CALL):
            # ![명령어] -> [명령어]
            text = content.replace(self.BOT_CALL, "").strip()
            print(f"message: {text}")

            await greetings_fn(channel, author, text)
            await views_fn(channel, text)
            await info_fn(channel, text)
