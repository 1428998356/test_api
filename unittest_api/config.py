'''
设置登录url，用户名，密码
'''
url = 'http://192.168.220.151:80' # url/端口
username = 'admin' # 用户名
password = 'admin' # 密码
login_url = f'{url}/adcapi/v2.0/?action=login' # 登录api的url

'''
邮件设置
'''
switch = 'off' # 邮件发送开关
sender = '1428998356@qq.com' # 发件人邮箱
emalPass = 'iduvkzdpupdaieeh' # 发件人密码/授权码
smtpServer = 'smtp.qq.com' # 邮箱服务器
accepter = ['15321038103@163.com'] # 收件人邮箱
