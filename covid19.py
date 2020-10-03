import requests
import bs4
from bs4 import BeautifulSoup


def get_covid19():
    url = 'http://ncov.mohw.go.kr/'
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    container: bs4.Tag = soup.find('ul', class_='liveNum')
    elements: list = container.select('li')

    # 확진환자
    patient_sum = elements[0].select('span')[0].text.replace('(누적)', '')
    patient_inc = elements[0].select('span')[2].text.replace('전일대비 ', '')

    # 격리해제
    cured_sum = elements[1].select('span')[0].text
    cured_inc = elements[1].select('span')[1].text

    # 치료 중(격리 중)
    quarantine_sum = elements[2].select('span')[1].text
    quarantine_inc = elements[2].select('span')[2].text

    # 사망
    dead_sum = elements[3].select('span')[0].text
    dead_inc = elements[3].select('span')[1].text

    patient = {'sum': patient_sum, 'inc': patient_inc}
    cured = {'sum': cured_sum, 'inc': cured_inc}
    quarantine = {'sum': quarantine_sum, 'inc': quarantine_inc}
    dead = {'sum': dead_sum, 'inc': dead_inc}

    # 메세지 설정
    message_ctx = f"확진환자: {patient['sum']:>6}명{patient['inc']}\n" \
                  f"격리해제: {cured['sum']:>6}명{cured['inc']}\n" \
                  f"치료 중 : {quarantine['sum']:>6}명{quarantine['inc']}\n" \
                  f"사망    : {dead['sum']:>6}명{dead['inc']}"

    message = f"```nim\n{message_ctx}```\n"
    return message


if __name__ == '__main__':
    covid19 = get_covid19()
    print(covid19)
