from typing import Tuple
import requests
from bs4 import BeautifulSoup

from hodolbot.classes import Model
from hodolbot.types import StockData


class StockModel(Model):
    eng2kor = {'kospi': '코스피', 'kosdaq': '코스닥', 'kospi200': '코스피200'}
    base_url = f'https://finance.naver.com/sise/sise_index.nhn?code='
    
    @classmethod
    def get(cls, stock_type: str) -> StockData:
        url = cls.base_url + stock_type.upper()
        html = requests.get(url)
        soup = BeautifulSoup(html.text, 'html.parser')

        nv = soup.find('em', {'id': 'now_value'}).text.strip()
        c_raw: str = soup.find('span', {'id': 'change_value_and_rate'}).text.strip()
        cv = c_raw.split(' ')[0]
        cr = c_raw.split(' ')[1]
        cv, cr = cls.decorate(cv, cr)

        return {
            'name': cls.eng2kor[stock_type],
            'nv': nv,
            'cv': cv,
            'cr': cr
        }

    # 주식 변동 문자열 꾸미기
    @staticmethod
    def decorate(value: str, rate: str) -> Tuple[str, str]:
        if rate[0] == '+':
            value = '▲'+value
            rate = rate.replace('상승', '')
        elif rate[0] == '-':
            value = '▼'+value
            rate = rate.replace("하락", '')
        else:
            value = '-'+value
        return value, rate
