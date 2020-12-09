import requests

# # 1.验证会员输入正确的手机号，正确的密码，登录成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone": "18123456789",
#     "pwd": "123456"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 1
# assert r["code"] == '10001'
# assert r["msg"] == '登录成功'

# # 2.验证会员手机号为空，输入正确18位的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone": None,
#     "pwd": "123456789123456789"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20103'
# assert r["msg"] == '手机号不能为空'

# # 3.验证会员输入过短的手机号，输入正确的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'1812345678',
#     "pwd": "123456"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20111'
# assert r["msg"] == '用户名或密码错误'

# # 4.验证会员输入过长的手机号，输入正确的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'181234567890',
#     "pwd": "123456"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20111'
# assert r["msg"] == '用户名或密码错误'

# # 5.验证会员输入未注册的手机号，输入正确的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'13572338555',
#     "pwd": "123456"
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20111'
# assert r["msg"] == '用户名或密码错误'

# # 6.验证会员输入正确的手机号，密码为空时，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'18123456789',
#     "pwd": None
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20103'
# assert r["msg"] == '密码不能为空'

# # 7.验证会员输入正确的手机号，过短的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'18123456789',
#     "pwd": '12345'
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20111'
# assert r["msg"] == '用户名或密码错误'

# # 8.验证会员输入正确的手机号，过长的密码，登录失败
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
# user = {
#     "mobilephone":'18123456789',
#     "pwd": '1234567891234567890'
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 0
# assert r["code"] == '20111'
# assert r["msg"] == '用户名或密码错误'
