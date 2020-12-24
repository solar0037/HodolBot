from hodolbot.classes import View
from hodolbot.controllers import stock_handler

class StockView(View):
    command = "주식"

    @staticmethod
    def get():
        return stock_handler()
