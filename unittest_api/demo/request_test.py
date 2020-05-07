import requests
import config
import json

class HttpRequest:
    def choice_method(self, inKey, action, body, method='post'):
        '''
        传入接口所需参数，并返回结果
        :param inKey:
        :param action:
        :param body:
        :param method:
        :return:
        '''
        url = f'{config.url}/adcapi/v2.0/?authkey={inKey}&action={action}'
        if method.lower() == 'get':
            return requests.get(url)
        elif method.lower() == 'post':
            return requests.post(url, json=json.loads(body))
        elif method.lower() == 'delete':
            pass
        elif method.lower() is 'put':
            pass
        else:
            print('请求方法不存在')

    def get_key(self):
        '''
        登录获取key值
        :return:
        '''
        username = config.username
        password = config.password
        url = config.login_url
        body = {
            "username": username,
            "password": password
        }
        res = requests.post(url, json=body)
        print(f'获取authkey:{res.text}')
        key = res.json()['authkey']
        return key


    def logout(self, key):
        '''
        注销登录
        :param key:
        :return:
        '''
        url = f'{config.url}/adcapi/v2.0/?authkey={key}&action=logout'
        re = requests.get(url)
        print(f'注销成功：{re.text}')


if __name__ == '__main__':
    body = '{"server": "12.2.2.2","status": 0,"prefer": 1,"minpoll": 5,"maxpoll": 9}'
    action = 'system.ntp.add'
    print(body)
    print(type(body))
    hr = HttpRequest()
    key = hr.get_key()
    result = hr.choice_method(inKey=key, action=action, body=body)
    print(result.text)
    hr.logout(key)


