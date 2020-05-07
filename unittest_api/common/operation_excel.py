import xlrd
import xlwt
from xlutils.copy import copy

class OperattionExcel:
    def __init__(self, inFile, sheetId=0):
        self.fileName = inFile
        self.sheetId = sheetId
        self.workBook = xlrd.open_workbook(self.fileName)
        self.sheet = self.workBook.sheet_by_index(self.sheetId)

    def get_sheet_id(self):
        return self.sheetId

    def get_rows(self):
        return self.sheet.nrows

    def get_cols(self):
        return self.sheet.ncols

    def get_row_values(self, row):
        return self.sheet.row_values(row)

    def copy_excel(self):
        return copy(self.workBook)


if __name__ == '__main__':
    file = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\excel_case\ntp.xls'
    oe = OperattionExcel(file)
    values = oe.get_row_values(1)
    print(values[2])
    print(type(values[2]))



