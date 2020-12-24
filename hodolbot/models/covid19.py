import requests
from bs4 import BeautifulSoup, Tag

from hodolbot.classes import Model
from hodolbot.types import Covid19Data


class Covid19Model(Model):
    url = 'http://ncov.mohw.go.kr/'
    
    @classmethod
    def get(cls) -> Covid19Data:
        html = requests.get(cls.url)
        soup = BeautifulSoup(html.text, 'html.parser')
        container: Tag = soup.find('ul', class_='liveNum')
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

        return {
            "patient": patient,
            "cured": cured,
            "quarantine": quarantine,
            "dead": dead
        }
