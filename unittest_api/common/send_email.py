import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import config

def send_mail(filePath):
    # 发送邮箱
    sendMail = config.sender
    password = config.emalPass
    # 接收邮箱
    acceptMail = config.accepter

    content = 'this is Test Result!!!'
    textApart = MIMEText(content)

    sendFile = filePath
    sendFileName = filePath.split('\\')[-1]
    Apart = MIMEApplication(open(sendFile, 'rb').read())
    Apart.add_header('Content-Disposition', 'attachment', filename=sendFileName)

    m = MIMEMultipart()
    m.attach(Apart)
    m['Subject'] = '测试报告'

    try:
        smtpServer = config.smtpServer
        server = smtplib.SMTP(smtpServer)
        server.login(sendMail, password)
        server.sendmail(sendMail, acceptMail, m.as_string())
        print('邮件发送成功')
        server.quit()
    except smtplib.SMTPException as e:
        print('邮件发送失败,error:', e)  # 打印错误


