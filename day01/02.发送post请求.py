'''
发送post请求
'''

import requests

# 登录的接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "18012345678",
    "pwd": "123456"
}
# data 传表单参数
r = requests.post(url, data=user)
print(r.text)

# 用data传表单参数
url = "http://www.httpbin.org/post"
user = {
    "mobilephone": "18012345678",
    "pwd": "123456"
}
r = requests.post(url, data=user)
print(r.text)
print("*********************************************************")
# 用json传参数,content-type:application/json
r = requests.post(url, json=user)
print(r.text)

# 练习:充值接口,给注册的用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "18012345678",
    "amount": 300000
}
r = requests.post(url, data=user)
print(r.text)
print("*********************************************************")
r = requests.post(url, json=user)
print(r.text)

# assert r.json()['status'] == 1
# assert r.json()['data']['regname'] == "Hello"
# assert r.json()['data']['mobilephone'] == "18012345678"
# print(r.json()['data']['leaveamount'])
