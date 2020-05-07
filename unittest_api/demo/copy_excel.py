# -*- coding:utf-8 -*-#
# Date: 2020/4/27
from xlutils.copy import copy
import xlrd
import os
import xlwt
'''
复制excel文件
'''
path = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\excel_case\ntp.xls'
workBook = xlrd.open_workbook(path)
sheetName = workBook.sheet_by_name('Sheet1')
ce = copy(workBook)
# ceSheet = ce.get_sheet(0)
# # ceSheet.write(1, 4, 'success')
localPath = os.path.dirname(os.getcwd())
print(localPath)
resultExcelPath = os.path.join(localPath, 'result_excel')
print(resultExcelPath)
if not os.path.isdir(resultExcelPath):
    os.mkdir(resultExcelPath)
newExcelName = os.path.join(resultExcelPath, path.split('\\')[-1])
print(newExcelName)
ce.save(newExcelName)
