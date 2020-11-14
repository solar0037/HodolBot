import urllib.request
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


# 주요종목 추가(코스피, 코스닥, 코스피200)
def add_major(stock_type: str):
    eng2kor = {'kospi': '코스피', 'kosdaq': '코스닥', 'kospi200': '코스피200'}

    url = f'https://finance.naver.com/sise/sise_index.nhn?code={stock_type.upper()}'
    """     req = urllib.request.Request(url)
    html = urlopen(req)
    soup = BeautifulSoup(html, 'html.parser') """
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')

    nv = soup.find('em', {'id': 'now_value'}).text.strip()
    c_raw: str = soup.find('span', {'id': 'change_value_and_rate'}).text.strip()
    cv = c_raw.split(' ')[0]
    cr = c_raw.split(' ')[1]
    cv, cr = decorate(cv, cr)

    stocks = {
        'name': eng2kor[stock_type],
        'nv': nv,
        'cv': cv,
        'cr': cr
    }
    return stocks


# 주식 가져오기
def get_stock():
    stocks = {
        'kospi': add_major('kospi'),
        'kosdaq': add_major('kosdaq'),
        'kospi200': add_major('kospi200')
    }
    line = '-'*50

    info = ""
    for data in stocks.values():
        info += f"{data['name']:<10} {data['nv']:>10} {data['cv']:>5} {'('+data['cr']+')':<14}\n"

    message_ctx = f"주식 정보\n" \
                  f"현재 코스피, 코스닥, 코스피200 정보입니다.\n" \
                  f"{line}\n" \
                  f"{info}" \
                  f"{line}\n" \
                  f"정보 제공: 네이버 금융\n"

    message = f"```nim\n{message_ctx}```"
    return message


# 주식 변동 문자열 꾸미기
def decorate(value: str, rate: str):
    if rate[0] == '+':
        value = '▲'+value
        rate = rate.replace('상승', '')
    elif rate[0] == '-':
        value = '▼'+value
        rate = rate.replace("하락", '')
    else:
        value = '-'+value
    return value, rate
