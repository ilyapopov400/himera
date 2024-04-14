import requests
import json
from fake_useragent import UserAgent

import os
from datetime import date
import datetime
import key

KEY = key.KEY


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
        with open(file=patch_file, mode="w") as file:
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
            print('ERROR {}'.format(response.status_code))
            raise ValueError('ERROR STATUS CODE {}'.format(response.status_code))

    def __call__(self, *args, **kwargs):
        result = json.loads(self._get_json())
        return result


def mane():
    data = {
        "phone": {
            "phone": "79123456789"
        }

    }

    data1 = {
        "name_standart": {
            "firstname": "Иванов",
            "lastname": "Иван",
            "middlename": "Иванович",
            "day": "",
            "mounth": "",
            "year": "",
        },
    }
    result = ParserHimera(data=data)()
    # writer_answer(answer=result)
    print(result)


if __name__ == "__main__":
    mane()
