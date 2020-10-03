from bs4 import BeautifulSoup
import requests


class Ranking:
    def __init__(self, channel):  # 디버깅: channel=None
        self.channel = channel
        self.message = ""

    # 프로그래밍
    def programming(self):
        url = "https://www.tiobe.com/tiobe-index/"
        html = requests.get(url)
        soup = BeautifulSoup(html.text, "html.parser")
        table = soup.find("table", {"id": "top20"})
        tr_list = table.find("tbody").find_all("tr")

        lang_list = []
        for i in range(0, len(tr_list)):
            lang_list.append(tr_list[i].find_all("td")[3].text)

        # 메세지 설정
        self.message += "```javascript\n"
        self.message += "프로그래밍 언어 순위\n" \
                        "2020년 TIOBE 제공 프로그래밍 언어 순위입니다.\n" \
                        "--------------------------------------------------\n"
        for i, data in enumerate(lang_list):
            self.message += "%4s %s\n" % (str(i+1)+"위:", data)
        self.message += "--------------------------------------------------\n"\
                        "정보 제공: TIOBE\n"
        self.message += "```"

    # 애니
    def anime(self):
        url = "http://anime.onnada.com/rank.php"
        html = requests.get(url)
        soup = BeautifulSoup(html.content.decode('utf-8', 'replace'), 'html.parser')

        tables = soup.find_all('table', class_='web-array')
        tr_list = tables[0].find_all('tr')
        td_list = []
        for i in range(3, 43, 2):
            td_list.append(tr_list[i])
        anime_list = []
        for item in td_list:
            anime_list.append(item.find_all('td')[2].find('a').text)

        # 메세지 설정
        self.message += "```javascript\n"
        self.message += "애니메이션 순위\n" \
                        "현재 온나다 제공 애니메이션 순위입니다.\n" \
                        "--------------------------------------------------\n"
        for i, data in enumerate(anime_list):
            self.message += "%4s %s\n" % (str(i + 1) + "위:", data)
        self.message += "--------------------------------------------------\n" \
                        "정보 제공: 온나다\n"
        self.message += '```'

    # 메세지 보내기
    async def show(self):
        await self.channel.send(self.message)

    # 디버깅 전용
    def debug(self):
        print(self.message)


if __name__ == '__main__':
    ranking = Ranking(None)
    ranking.programming()
    ranking.debug()

    ranking = Ranking(None)
    ranking.anime()
    ranking.debug()
