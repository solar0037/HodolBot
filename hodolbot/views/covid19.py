from hodolbot.classes import View
from hodolbot.controllers import covid19_handler

class Covid19View(View):
    command = "코로나"

    @staticmethod
    def get():
        return covid19_handler()
