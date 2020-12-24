from typing import Dict
from hodolbot.models import StockModel
from hodolbot.types import StockData


def stock_handler() -> str:
    data: Dict[str, StockData] = {
        'kospi': StockModel.get('kospi'),
        'kosdaq': StockModel.get('kosdaq'),
        'kospi200': StockModel.get('kospi200')
    }

    line = '-'*50

    info = ""
    for stock in data.values():
        info += f"{stock['name']:<10} {stock['nv']:>10} {stock['cv']:>5} {'('+stock['cr']+')':<14}\n"

    message_ctx = f"주식 정보\n" \
                f"현재 코스피, 코스닥, 코스피200 정보입니다.\n" \
                f"{line}\n" \
                f"{info}" \
                f"{line}\n" \
                f"정보 제공: 네이버 금융\n"

    message = f"```nim\n{message_ctx}```"
    return message
