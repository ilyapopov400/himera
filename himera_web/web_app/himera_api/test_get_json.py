"""
тесты для нулевого баланса
"""
import unittest
from get_json import ParserHimera
from example_request_json import data as test_data

for key in test_data.keys():
    class MyTestCase(unittest.TestCase):
        def test_ParserHimera(self):
            dt = dict()
            dt[key] = test_data[key]
            result = ParserHimera(data=dt)()
            correct_answer = {'error': 'Not enough money'}
            self.assertEqual(result, correct_answer)


class MyTestCase1(unittest.TestCase):
    def test_ParserHimera_name_standart1(self):
        data = {"name_standart": {
            # Запрос по ФИО
            "firstname": "Иванов",  # - имя, - обязательное
            "lastname": "Иван",  # - фамилия, - обязательное
            "middlename": "Иванович",  # - отчество, - обязательное
            "day": "01",  # - день рождения
            "mounth": "01",  # - месяц рождения
            "year": "1900",  # - год рождения
        }
        }
        result = ParserHimera(data=data)()
        correct_answer = {'status': 'not_found'}
        self.assertEqual(result, correct_answer)

    def test_ParserHimera_name_standart2(self):
        data = {"name_standart": {
            # Запрос по ФИО
            "firstname": "Иванов",  # - имя, - обязательное
            "lastname": "Иван",  # - фамилия, - обязательное
            "middlename": "Иванович",  # - отчество, - обязательное
            "day": "",  # - день рождения
            "mounth": "",  # - месяц рождения
            "year": "",  # - год рождения
        }
        }
        result = ParserHimera(data=data)()
        correct_answer = {'error': 'Not enough money'}
        self.assertEqual(result, correct_answer)


if __name__ == '__main__':
    unittest.main()
