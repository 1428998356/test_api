# -*- coding:utf-8 -*-#
# Date: 2020/4/27
import time
import zipfile
import os

def zip_file(*inFile):
    localTime = time.strftime('%Y_%m_%d_%H-%M-%S')
    zipPath = os.path.join(os.getcwd(), 'zip_report')
    if not os.path.isdir(zipPath):
        os.mkdir(zipPath)
    zipName = localTime+'.zip'
    zipFile = os.path.join(zipPath, zipName)
    # print(zipFile)
    with zipfile.ZipFile(zipFile, 'a') as target:
        for file in inFile:
            fileName = file.split('\\')[-1]
            # print(fileName)
            target.write(file, arcname=fileName)
    return zipFile

if __name__ == '__main__':
    file = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\html_report\2020_04_27_13-53-59_htmlReport.html'
    file1 = r'C:\Users\Administrator\PycharmProjects\test\unittest_api\log_file\2020_04_27_11-29-55.txt'
    zip_file(file, file1)


