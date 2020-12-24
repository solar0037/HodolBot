from hodolbot.models import Covid19Model
from hodolbot.types import Covid19Data


def covid19_handler() -> str:
    data: Covid19Data =  Covid19Model.get()

    # 메세지 설정
    message_ctx = f"확진환자: {data['patient']['sum']:>6}명{data['patient']['inc']}\n" \
                f"격리해제: {data['cured']['sum']:>6}명{data['cured']['inc']}\n" \
                f"치료 중 : {data['quarantine']['sum']:>6}명{data['quarantine']['inc']}\n" \
                f"사망    : {data['dead']['sum']:>6}명{data['dead']['inc']}"

    message = f"```nim\n{message_ctx}```\n"
    return message
