import logging
import time
import os

localPath = os.getcwd()

class Log:
    def __init__(self):
        self.localTime = time.strftime('%Y_%m_%d_%H-%M-%S')
        # 第一步，创建一个logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO) # Log等级总开关
        # 第二步，创建一个handler，用于写入日志文件
        logFilePath = os.path.join(localPath, 'log_file')
        if not os.path.isdir(logFilePath):
            os.mkdir(logFilePath)
        self.logFileName = os.path.join(logFilePath, self.localTime+'.txt')
        logfile = './log.txt'
        fh = logging.FileHandler(self.logFileName, mode='a') # open的打开模式这里可以进行参考
        fh.setLevel(logging.DEBUG) # 输出到file的log等级的开关
        # 第三步，再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关
        # 第四步，定义handler的输出格式
        formatter = logging.Formatter("%(asctime)s - %(levelname)s: %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 将日志打印到控制台
        # stream_handler = logging.StreamHandler()
        # self.logger.addHandler(stream_handler)
        # 第五步，将logger添加到handler里面
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # 日志
        # self.logger.debug('这是 logger debug message')

    def get_info_logger(self, msg):
        self.logger.info(msg)
        # return self.logger

    def get_error_logger(self, msg):
        self.logger.error(msg)

    def get_logFileName(self):
        return self.logFileName

    def get_logger(self):
        return self.logger
