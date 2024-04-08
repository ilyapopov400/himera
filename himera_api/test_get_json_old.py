"""
тесты для нулевого баланса
"""
import unittest
from get_json_old import ChangeRequest
from example_request_json import data


class MyTestCase(unittest.TestCase):
    def test_name_standart(self):
        parser = ChangeRequest
        result = parser.name_standart(question="Иван Иванов Иванович ")
        correct_answer = {'error': 'Not enough money'}
        self.assertEqual(result, correct_answer)

    def test_phone(self):
        parser = ChangeRequest
        result = parser.phone(question="79123456789")
        correct_answer = {'error': 'Not enough money'}
        self.assertEqual(result, correct_answer)


if __name__ == '__main__':
    unittest.main()
