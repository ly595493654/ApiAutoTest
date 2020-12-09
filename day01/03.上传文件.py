'''
接口的功能是上传文件,比如上传头像,附件等
'''

import requests

url = "http://www.httpbin.org/post"
# 将本地的文件上传到服务器上
file1 = "d:/ApiAutoTest/dat01/test.txt"
file1 = "D:\\ApiAutoTest\\dat01\\test.txt"
file1 = r"D:\ApiAutoTest\dat01\test.txt"
with open(file1, mode='r', encoding='utf-8') as f:
    # 字典,上传的文件:文件相关的参数组成的元组
    # text/plan 是文件的类型
    load = {
        "file1": (file1, f, "text/plan")
    }
    r = requests.post(url, files=load)
    print(r.text)
    print("*******************************************************************")

# 上传图片
file2 = "d:/ApiAutoTest/dat01/test.jpg"
with open(file2, mode='rb') as f:
    load = {
        # 文件名:file-tuple
        # file-tuple 可以是二元组、三元组、四元组
        # image/png MIME类型,文件类型,application/json application/..
        "file2": (file2, f, "image/png")
    }
    r = requests.post(url, files=load)
    print(r.text)
    print("*******************************************************************")

# 可以一次上传多个文件,文本和图片一起上传
with open(file1, mode='r', encoding='utf-8') as f1:
    with open(file2, mode='rb') as f2:
        load = {
            "file1": (file1, f1),
            "file2": (file2, f2, "image/png")
        }
        r = requests.post(url,files=load)
        print(r.text)
