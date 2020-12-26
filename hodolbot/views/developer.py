from discord.embeds import Embed
from hodolbot.classes import View
from hodolbot.controllers import developer_handler

class DeveloperView(View):
    command = "개발자"

    @staticmethod
    def get() -> Embed:
        return developer_handler()
