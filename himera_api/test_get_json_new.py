"""
тесты для нулевого баланса
"""
import unittest
from get_json_new import ParserHimera
from example_request_json import data as test_data

for key in test_data.keys():
    class MyTestCase(unittest.TestCase):
        def test_ParserHimera(self):
            dt = dict()
            dt[key] = test_data[key]
            result = ParserHimera(data=dt)()
            correct_answer = {'error': 'Not enough money'}
            self.assertEqual(result, correct_answer)


if __name__ == '__main__':
    unittest.main()
