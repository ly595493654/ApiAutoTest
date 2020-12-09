'''
注册的测试用例
'''
import requests

# # 1.验证用户使用正确的手机号、6位长度的密码、注册名为空时，注册成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18123456789",
#     "pwd": "123456",
#     "regname": None
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 1
# assert r["code"] == '10001'
# assert r["msg"] == '注册成功'

# # 2.验证用户使用正确的手机号、18位长度的密码、注册名为空时，注册成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18123456780",
#     "pwd": "123456789123456789",
#     "regname": None
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 1
# assert r["code"] == '10001'
# assert r["msg"] == '注册成功'

# 3.验证用户使用正确的手机号、6位的密码、正确的注册名，注册成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18123456781",
#     "pwd": "123456",
#     "regname": '凯凯'
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 1
# assert r["code"] == '10001'
# assert r["msg"] == '注册成功'

# # 4.验证用户使用正确的手机号、18位的密码、正确的注册名，注册成功
# url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18123456782",
#     "pwd": "123456789123456789",
#     "regname": '凯凯凯'
# }
# r = requests.get(url, params=user)
# r = r.json()
# print(r)
# assert r["status"] == 1
# assert r["code"] == '10001'
# assert r["msg"] == '注册成功'

# 5.验证用户手机号为空时、输入6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": None,
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20103'
assert r["msg"] == '手机号不能为空'

# 6.验证用户手机号为空时、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": None,
    "pwd": "123456",
    "regname": "凯凯"
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20103'
assert r["msg"] == '手机号不能为空'

# 7.验证用户输入过短的手机号、6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540393',
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 8.验证用户输入过短手机号、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540393',
    "pwd": "123456",
    "regname": "凯凯"
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 9.验证用户输入过长的手机号、6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '181654039355',
    "pwd": "123456",
    "regname": "凯凯"
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 10.验证用户输入过长的手机号、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '181654039355',
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 11.验证用户输入非法字符手机号、6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540/*-+',
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 12.验证用户输入非法字符手机号、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540/*-+',
    "pwd": "123456",
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 13.验证用户输入有汉字的手机号、6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540凯凯',
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 14.验证用户输入有汉字的手机号、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '1816540凯凯',
    "pwd": "123456",
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 15.验证用户输入非号段手机号、6位长度的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '28165403935',
    "pwd": "123456",
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 16.验证用户输入非号段手机号、6位长度的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '28165403935',
    "pwd": "123456",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20109'
assert r["msg"] == '手机号码格式不正确'

# 17.验证用户输入正确的手机号，过短的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": "12345",
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20108'
assert r["msg"] == '密码长度必须为6~18'

# 18.验证用户输入正确的手机号，过短的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": "12345",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20108'
assert r["msg"] == '密码长度必须为6~18'

# 19.验证用户输入正确的手机号，过长的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": "1234567891234567890",
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20108'
assert r["msg"] == '密码长度必须为6~18'

# 20.验证用户输入正确的手机号，过长的密码、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": "1234567891234567890",
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20108'
assert r["msg"] == '密码长度必须为6~18'

# 21.验证用户输入正确的手机号，密码为空、正确的注册名，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": None,
    "regname": '凯凯'
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20103'
assert r["msg"] == '密码不能为空'

# 22.验证用户输入正确的手机号，密码为空、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18165403935',
    "pwd": None,
    "regname": None
}
r = requests.get(url, params=user)
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20103'
assert r["msg"] == '密码不能为空'

# 23.验证用户输入正确的手机号，正确的密码、注册名为空时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18123456789',
    "pwd": '123456',
    "regname": None
}
r = requests.get(url, params=user)  # 发送请求
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20110'
assert r["msg"] == '手机号码已被注册'

# 24.验证用户输入正确的手机号，正确的密码、正确的注册名时，注册失败
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": '18123456789',
    "pwd": '123456',
    "regname": '凯凯'
}
r = requests.get(url, params=user)  # 发送请求
r = r.json()
print(r)
assert r["status"] == 0
assert r["code"] == '20110'
assert r["msg"] == '手机号码已被注册'

