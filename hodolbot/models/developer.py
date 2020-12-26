from hodolbot.classes import Model


class DeveloperModel(Model):
    @classmethod
    def get(cls) -> dict:
        return {
            "dimipedia": "https://dimipedia.net/wiki/%EC%82%AC%ED%98%B8%EC%A4%80",
            "github": "https://github.com/sqrtpi177",
            "blog": "https://blog.naver.com/moy0037",
            "facebook": "https://www.facebook.com/profile.php?id=100029757106182",
            "youtube": "https://www.youtube.com/channel/UCkxI0ozgMOV3Akpyr6QQ5RQ"
        }
