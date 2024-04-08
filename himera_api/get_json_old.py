import requests
import json
from fake_useragent import UserAgent
from key import KEY

KEY = KEY


class ChangeRequest:
    """
    набор методов для отработки 12-ти типов запросов
    при использовании класса GetJson, который посылает запрос на api
    """

    @staticmethod
    def name_standart(question: str):
        """
        запрос по учетным данным
        передаются в виде строки через пробел
        от 3-х до 6-ти полей
        пример "Иванов Иван Иванович"
        :param question: str
        :return:
        """
        url = "https://api.himera-search.info/2.0/name_standart"
        data = dict()
        data_sample = {
            "firstname": "",
            "lastname": "",
            "middlename": "",
            "day": "",
            "mounth": "",
            "year": "",
        }
        try:
            full_name = question.strip().split()
            if 7 <= len(full_name) <= 2:
                raise ValueError("должно от трех до шести полей данных")
            else:
                for number, element in enumerate(data_sample):
                    if number < len(full_name):
                        data[element] = full_name[number]
                    else:
                        data[element] = ""
                result = GetJson(url=url, data=data)()

                return result
        except:
            raise ValueError("неверный формат ввода данных")

    @staticmethod
    def phone(question: str):
        """
        запрос по номеру телефона
        передается в виде строки
        пример "79123456789"
        :param question:
        :return:
        """
        url = "https://api.himera-search.info/2.0/phone"
        data = {
            "phone": question,
        }
        result = GetJson(url=url, data=data)()

        return result


class GetJson:
    KEY = KEY
    '''
    запрос на сервер по api
    возвращаем json при вызове экземпляра класса
    '''

    def __init__(self, url: str, data: dict):
        self.url = url
        self.data = data
        self.data["key"] = self.KEY

    def _fake_user_agent(self):  # crate fake user agent
        ua = UserAgent()
        fake_ua = {'user-agent': ua.random}
        return fake_ua

    def _get_json(self) -> json:
        headers = self._fake_user_agent()
        response = requests.post(url=self.url,
                                 headers=headers, data=self.data)
        response.encoding = 'utf-8'
        if response:
            return response.text
        else:
            print('ERROR {}'.format(response.status_code))
            raise ValueError('ERROR STATUS CODE {}'.format(response.status_code))

    def __call__(self, *args, **kwargs):
        result = json.loads(self._get_json())
        return result


def mane():
    parser = ChangeRequest
    result = parser.name_standart(question="Иван Иванов Иванович")
    print(result)


if __name__ == "__main__":
    mane()
