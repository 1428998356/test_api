import unittest
from common.get_result import ResultList
from ddt import ddt, unpack, data
from run_case import localPath
import os

ntpExcel = os.path.join(localPath, 'excel_case', 'ntp.xls')
ntp = ResultList(ntpExcel)
ntpList = ntp.get_result()

@ddt
class TestNtp(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('*' * 20 + '开始执行' + '*' * 20)

    @data(*ntpList)
    def test_(self, value):
        self.assertEqual(value[1], value[2])

    @classmethod
    def tearDownClass(cls):
        print('*' * 20 + '结束执行' + '*' * 20)


if __name__ == '__main__':
    unittest.main()
