import os
from common.http_request import HttpRequest
from common.operation_excel import OperattionExcel
from common.excel_num import ReadDatas
from common.log import Log


log = Log()
logger = log.get_logger()
logFileName = log.get_logFileName()
localPath = os.path.dirname(__file__)

class ResultList:
    def __init__(self, filePath):
        self.fileName = filePath

    def get_result(self):
        opreateExcel = OperattionExcel(self.fileName)
        sheetId = opreateExcel.get_sheet_id()
        copyExcel = opreateExcel.copy_excel()
        copySheetName = copyExcel.get_sheet(sheetId)
        nrows = opreateExcel.get_rows()
        resultExcelPath = os.path.join(localPath, '..', 'result_excel')
        if not os.path.isdir(resultExcelPath):
            os.mkdir(resultExcelPath)
        newExcelName = os.path.join(resultExcelPath, self.fileName.split('\\')[-1])
        resultAndExpect = []
        re = HttpRequest()
        key = re.get_key()
        for i in range(1, nrows):
            data = opreateExcel.get_row_values(i)  # 获取excel中一行数据并以列表形式返回
            datasList = ReadDatas(data)  # 接收列表，并处理列表中元素
            action = datasList.get_action()# 获取action
            body = datasList.get_body()# 获取参数
            caseName = datasList.get_case_name()# 获取用例名称
            result = re.choice_method(key, action, body)# 接口测试，获取结果
            expect = datasList.get_expect()#获取期望结果
            resultAndExpect.append([caseName, result.text, expect])# 用例名称，测试结果，期望结果写入列表
            try:
                if result.text == expect:# 测试结果与期望结果对比
                    copySheetName.write(i, datasList.result_col(), 'success')# 写入成功结果
                    # log.get_info_logger(f'{caseName}:success')  # 将测试结果写入日志
                    logger.info(f'{caseName}:success')
                else:
                    copySheetName.write(i, datasList.result_col(), 'fail')#写入失败结果
                    copySheetName.write(i, datasList.reason_col(), result.text)#写入失败原因
                    # log.get_info_logger(f'{caseName}:{result.text}')  # 将测试结果写入日志
                    logger.info(f'{caseName}:{result.text}')
            except Exception as e:
                # log.get_error_logger(e)
                logger.error(e)
                print(e)
        re.logout(key) # 注销登录
        copyExcel.save(newExcelName) # 保存写入结果的excel文件
        return resultAndExpect

if __name__ == '__main__':
    fileName = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\excel_case\user.xls'
    res = ResultList(fileName)
    re = res.get_result()
    # print(re)
