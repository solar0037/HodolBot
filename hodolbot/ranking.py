from bs4 import BeautifulSoup
import requests


def get_programming():
    url = 'https://www.tiobe.com/tiobe-index/'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    table = soup.find('table', {'id': 'top20'})
    tr_list = table.find('tbody').find_all('tr')

    lang_list = []
    for i in range(0, len(tr_list)):
        lang_list.append(tr_list[i].find_all('td')[3].text)

    # 메세지 설정
    line = '-'*50

    info = ""
    for i, data in enumerate(lang_list):
        info += f"{str(i+1)+'위:':>4} {data:<40}\n"

    message_ctx = f"프로그래밍 언어 순위\n" \
                  f"2020년 TIOBE 제공 프로그래밍 언어 순위입니다.\n" \
                  f"{line}\n" \
                  f"{info}" \
                  f"{line}\n" \
                  f"정보 제공: TIOBE\n"

    message = f"```nim\n{message_ctx}```"
    return message


def get_anime():
    url = 'http://anime.onnada.com/rank.php'
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
    line = '-'*50

    info = ""
    for i, data in enumerate(anime_list):
        info += f"{str(i+1)+'위:':>4} {data:<50}\n"

    message_ctx = f"애니메이션 순위\n" \
                  f"현재 온나다 제공 애니메이션 순위입니다.\n" \
                  f"{line}\n" \
                  f"{info}" \
                  f"{line}\n" \
                  f"정보 제공: 온나다\n"

    message = f"```nim\n{message_ctx}```"
    return message
