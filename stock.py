import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


class Stock:
    def __init__(self, channel):  # 디버깅: channel=None
        self.channel = channel
        self.stocks = []
        self.message = ""

    # 모든 주요종목 추가(코스피, 코스닥, 코스피200)
    def all_major(self):
        self.stock_major('kospi')
        self.stock_major('kosdaq')
        self.stock_major('kospi200')

        # 메세지 설정
        self.message += "```javascript\n"
        self.message += "주식 정보\n" \
                        "현재 코스피, 코스닥, 코스피200 정보입니다.\n" \
                        "--------------------------------------------------\n"
        for data in self.stocks:
            self.message += "{:10s} {:10s} {:5s}({:5s})\n".format(
                data['name'], data['nv'], data['cv'], data['cr']
            )
        self.message += "--------------------------------------------------\n" \
                        "정보 제공: 네이버 금융\n"
        self.message += "```"

    # 주요종목 추가(코스피, 코스닥, 코스피200)
    def stock_major(self, stock_type):
        eng2kor = {'kospi': '코스피', 'kosdaq': '코스닥', 'kospi200': '코스피200'}

        url = "https://finance.naver.com/sise/sise_index.nhn?code=" + stock_type.upper()
        req = urllib.request.Request(url)
        html = urlopen(req)
        soup = BeautifulSoup(html, "html.parser")

        nv = soup.find("em", {"id": "now_value"}).text.strip()
        c_raw = soup.find("span", {"id": "change_value_and_rate"}).text.strip()
        cv = c_raw.split(' ')[0]
        cr = c_raw.split(' ')[1]
        cv, cr = decorate(cv, cr)
        self.stocks.append({'name': eng2kor[stock_type],
                            'nv': nv,
                            'cv': cv,
                            'cr': cr})

    # 메세지 보내기
    async def show(self):
        await self.channel.send(self.message)

    # 디버깅 전용
    def debug(self):
        for data in self.stocks:
            # embed.add_field(name=data['name'],
            #                 value="{}\n{} {}".format(data['nv'], data['cv'], data['cr']),
            #                 inline=True)
            print(data['name'])
            print(data['nv'], data['cv'], data['cr'])


# 주식 변동 문자열 꾸미기
def decorate(value, rate: str):
    if rate[0] == '+':
        value = '▲'+value
        rate = rate.replace("상승", "")
    elif rate[0] == '-':
        value = '▼'+value
        rate = rate.replace("하락", "")
    else:
        value = '-'+value
    return value, rate


if __name__ == '__main__':
    stock = Stock(None)
    stock.all_major()
    stock.debug()
