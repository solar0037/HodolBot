import requests
from bs4 import BeautifulSoup


class Covid19:
    def __init__(self, channel):  # 디버깅: channel=None
        self.channel = channel
        self.patient, self.cured, self.quarantine, self.passed_away = {}, {}, {}, {}
        self.message = ""

    def all(self):
        html = requests.get("http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=&brdGubun=&ncv")
        soup = BeautifulSoup(html.text, "html.parser")
        content = soup.find_all('div', {'id': 'content'})[0]
        case_table = content.find('div', class_='caseTable')

        ##################################################
        #                   확진환자                     #
        ##################################################
        patient_body = case_table.find_all('div')[0].find('ul', class_='ca_body')

        # 확진환자 누적
        patient_sum = patient_body\
            .find_all('li')[0]\
            .find('dd')\
            .text

        # 확진환자 전일대비
        patient_increase_body = patient_body\
            .find_all('li')[1]\
            .find('dd')
        patient_increase_sum = patient_increase_body\
            .find_all('li')[0]\
            .find('p')\
            .text
        patient_increase_world = patient_increase_body \
            .find_all('li')[1] \
            .find('p')\
            .text
        patient_increase_nation = patient_increase_body \
            .find_all('li')[2] \
            .find('p')\
            .text

        ###################################################
        #                   격리해제                      #
        ###################################################
        cured_body = case_table.find_all('div')[1].find('ul', class_='ca_body')

        # 격리해제 누적
        cured_sum = cured_body\
            .find_all('li')[0]\
            .find('dd')\
            .text
        # 격리해제 전일대비
        cured_increase = cured_body\
            .find_all('li')[1]\
            .find('dd')\
            .find('span')\
            .text

        ##################################################
        #                   격리중                       #
        ##################################################
        quarantine_body = case_table.find_all('div')[2].find('ul', class_='ca_body')

        # 격리중 누적
        quarantine_sum = quarantine_body\
            .find_all('li')[0]\
            .find('dd')\
            .text
        # 격리중 전일대비
        quarantine_increase = quarantine_body\
            .find_all('li')[1]\
            .find('dd')\
            .find('span')\
            .text

        ##################################################
        #                       사망                     #
        ##################################################
        passed_away_body = case_table.find_all('div')[3].find('ul', class_='ca_body')

        passed_away_sum = passed_away_body \
            .find_all('li')[0] \
            .find('dd') \
            .text
        passed_away_increase = passed_away_body \
            .find_all('li')[1] \
            .find('dd') \
            .find('span') \
            .text

        self.patient = dict(sum=patient_sum,
                            increase=dict(sum=patient_increase_sum,
                                          world=patient_increase_world,
                                          nation=patient_increase_nation))
        self.cured = dict(sum=cured_sum,
                          increase=cured_increase)
        self.quarantine = dict(sum=quarantine_sum,
                               increase=quarantine_increase)
        self.passed_away = dict(sum=passed_away_sum,
                                increase=passed_away_increase)

        # 메세지 설정
        self.message += "```javascript\n"
        self.message += '확진환자: {}명({})\n'.format(self.patient['sum'], self.patient['increase']['sum'])
        self.message += '격리해제: {}명({})\n'.format(self.cured['sum'], self.cured['increase'])
        self.message += '격리중: {}명({})\n'.format(self.quarantine['sum'], self.quarantine['increase'])
        self.message += '사망: {}명({})\n'.format(self.passed_away['sum'], self.passed_away['increase'])
        self.message += "```\n"

    # 메세지 보내기
    async def show(self):
        await self.channel.send(self.message)

    # 디버깅 전용
    def debug(self):
        print(self.message)


if __name__ == '__main__':
    covid19 = Covid19(None)
    covid19.all()
    covid19.debug()
