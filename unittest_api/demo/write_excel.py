# -*- coding:utf-8 -*-#
# Date: 2020/4/27
import xlwt
excelPath = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\result_excel\ntp.xls'
workBook = xlwt.Workbook()
sheetName = workBook.add_sheet('Sheet1', cell_overwrite_ok=True)
sheetName.write(3, 4, 'success')
workBook.save(excelPath)
