import config as cf
import config
import json

class ReadDatas:
    def __init__(self, inList):
        # 以列表形式获取excel一行数据
        self.dataList = inList
        # 列表中测试用例名称索引
        self.caseName = 1
        # 列表中action索引
        self.action = 2
        # 列表中所需参数索引
        self.body = 3
        # 列表中期望结果索引
        self.expect = 4
        # excel中结果所在列索引
        self.result = 5
        # excel中失败原因所在列索引
        self.reason = 6

    def get_action(self):
        return self.dataList[self.action]

    def get_body(self):
        return self.dataList[self.body].replace('\n', '')

    def get_expect(self):
        return self.dataList[self.expect].replace('\n', '')

    def get_case_name(self):
        return self.dataList[self.caseName]

    def result_col(self):
        return self.result

    def reason_col(self):
        return self.reason



