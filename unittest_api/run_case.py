import unittest
from HTMLTestRunner import HTMLTestRunner
from common.send_email import send_mail
import os
import time
import config
from common.zip_file import zip_file
from common.get_result import logFileName


localPath = os.path.dirname(__file__)
localTime = time.strftime('%Y_%m_%d_%H-%M-%S')

def get_case_list():
    '''
    读取case_list.txt获取要执行的测试用例
    :return:
    '''
    case_list_file = os.path.join(localPath, 'case_list.txt')
    case_list = []
    with open(case_list_file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line[0] != '#':
                case_list.append(line.strip())
    return case_list


def run_allCase(case_list):
    '''
    获取所有用例文件后全部执行
    :return:
    '''
    casePath = os.path.join(localPath, 'test_case')
    suit = unittest.TestSuite()
    for case in case_list:
        caseFile = case + '.py'
        dis = unittest.defaultTestLoader.discover(casePath, caseFile)
        suit.addTest(dis)
    htmlPath = os.path.join(localPath, 'html_report')
    if not os.path.isdir(htmlPath):
        os.mkdir(htmlPath)
    htmlReport = r'html_report\{}_htmlReport.html'.format(localTime)
    f = open(htmlReport, 'wb')
    runner = HTMLTestRunner(stream=f,
                            title='Test Result',
                            description='测试用例执行情况：')
    runner.run(suit)
    f.close()
    # 压缩html报告和日志文件
    logFilePath = os.path.join(localPath, 'log_file')
    logFile = os.path.join(logFilePath, logFileName)
    zipFile = zip_file(htmlReport, logFile)
    # 判断状态，是否发送邮件
    if config.switch == 'on':
        send_mail(zipFile)

if __name__ == '__main__':
    caseList = get_case_list()
    run_allCase(caseList)
