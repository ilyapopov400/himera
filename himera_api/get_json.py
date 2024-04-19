import requests
import json
from fake_useragent import UserAgent

import os
from datetime import date
import datetime

from json import JSONDecodeError

from key import KEY

KEY = KEY


class ParserHimera:
    """
    набор методов для отработки 12-ти типов запросов
    при использовании класса GetJson, который посылает запрос на api
    """

    def __init__(self, data: dict):
        self.data = data
        self.key = list(self.data.keys())[0]

    def _get_data(self, data: dict):
        url = "https://api.himera-search.info/2.0/{}".format(self.key)
        result = GetJson(url=url, data=data.get(self.key))()
        return result

    def _writer_answer(self, answer):
        """
        запись ответа от сервера в директорию "answers/today/key/key.py"
        :param answer:
        :return:
        """
        patch_dir = 'answers/{}/{}'.format(date.today(), self.key)
        patch_file = "{}/{}{}{}.py".format(patch_dir,
                                           self.key,
                                           datetime.datetime.now().time().hour,
                                           datetime.datetime.now().time().minute)
        os.makedirs(patch_dir, exist_ok=True)
        with open(file=patch_file, mode="w", encoding="utf-8") as file:
            file.write(json.dumps(answer))
            file.write("\n")

        os.makedirs("TEST_DATA/", exist_ok=True)
        with open(file="TEST_DATA/{}".format(self.key), mode="w", encoding="utf-8") as file:
            file.write(json.dumps(answer))
            file.write("\n")

    def __call__(self):
        result = self._get_data(data=self.data)
        self._writer_answer(answer=result)

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
            return json.dumps({"error": 'ERROR {}{}'.format(response.status_code, self.url)})

    def __call__(self, *args, **kwargs):
        try:
            json.loads(self._get_json())
            result = json.loads(self._get_json())
        except JSONDecodeError:
            answer = str(self._get_json())
            result = {"error": answer}
            result = json.dumps(result)
            result = json.loads(result)
        return result


def mane():
    data1 = {
        "phone": {
            "phone": "79123456789"
        }

    }

    data2 = {
        "name_standart": {
            "firstname": "Иванов",
            "lastname": "Иван",
            "middlename": "Иванович",
            "day": "01",
            "mounth": "01",
            "year": "1991",
        },
    }

    data3 = {
        "passport": {
            "passport": "1234567890",
        },
    }

    data4 = {
        "inn_fl": {
            "inn_fl": "1234567890",
        },
    }

    data5 = {
        "email": {
            "email": "demo@demo.ru",
        },
    }

    data6 = {
        "snils": {
            "snils": "12602903624",
        },
    }

    data7 = {
        "adres": {
            "city": "тамбов",
            "street": "рылеева",
            "home": "68",
            "flat": "31",
        },
    }

    data8 = {
        "avto": {
            "avto": "H688AA77",
        },
    }

    data9 = {
        "vin": {
            "win": "kgft5l05lfds46d",
        },
    }

    data10 = {
        "inn": {
            "inn": "1234567890",
        },
    }

    data11 = {
        "scoring": {
            "lastname": "иванов",
            "firstname": "иван",
            "middlename": "иванович",
            "birthday": "01.01.1991",
        },
    }

    data12 = {
        "credit": {
            "lastname": "иванов",
            "firstname": "иван",
            "middlename": "иванович",
            "birthday": "01.01.1991",
        },
    }

    data13 = {
        "credit": {
            "lastname": "иванов",
            "firstname": "иван",
            "middlename": "иванович",
            "birthday": "01.01.1991",
        },
    }

    data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11, data12, data13]

    # result = ParserHimera(data=data9)()
    # print(result)
    for i in data:
        result = ParserHimera(data=i)()
        print(result)


if __name__ == "__main__":
    mane()
