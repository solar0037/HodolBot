from hodolbot.models import ProgrammingModel, AnimeModel
from hodolbot.types import ProgrammingData, AnimeData


def programming_handler() -> str:
    data: ProgrammingData = ProgrammingModel.get()
    # 메세지 설정
    line = '-'*50

    info = ""
    for i, lang in enumerate(data):
        info += f"{str(i+1)+'위:':>4} {lang:<40}\n"

    message_ctx = f"프로그래밍 언어 순위\n" \
                f"2020년 TIOBE 제공 프로그래밍 언어 순위입니다.\n" \
                f"{line}\n" \
                f"{info}" \
                f"{line}\n" \
                f"정보 제공: TIOBE\n"

    message = f"```nim\n{message_ctx}```"
    return message


def anime_handler() -> str:
    data: AnimeData = AnimeModel.get()

    # 메세지 설정
    line = '-'*50

    info = ""
    for i, data in enumerate(data):
        info += f"{str(i+1)+'위:':>4} {data:<50}\n"

    message_ctx = f"애니메이션 순위\n" \
                f"현재 온나다 제공 애니메이션 순위입니다.\n" \
                f"{line}\n" \
                f"{info}" \
                f"{line}\n" \
                f"정보 제공: 온나다\n"

    message = f"```nim\n{message_ctx}```"
    return message
