from hodolbot.classes import View
from hodolbot.controllers import programming_handler, anime_handler

class ProgrammingView(View):
    command = "프로그래밍"

    @staticmethod
    def get():
        return programming_handler()

class AnimeView(View):
    command = "애니"
    
    @staticmethod
    def get():
        return anime_handler()
