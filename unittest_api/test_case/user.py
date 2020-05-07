import unittest
from common.get_result import ResultList
from ddt import ddt, data

userExcel = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\excel_case\user.xls'
user = ResultList(userExcel)
userExcel = user.get_result()

@ddt
class TestNtp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('*' * 20 + '开始执行' + '*' * 20)

    @data(*userExcel)
    def test_user(self, value):
        self.assertEqual(value[1], value[2])

    @classmethod
    def tearDownClass(cls):
        print('*' * 20 + '结束执行' + '*' * 20)


if __name__ == '__main__':
    unittest.main()
