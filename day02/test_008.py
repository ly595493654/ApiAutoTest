import pytest
import requests

url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"

@pytest.fixture(params=[{"data":{"mobilephone":"13133333310","pwd":"123456"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111114","pwd":"123456789098765432"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111116","pwd":"123456"},"expect":{"msg":"手机号码已被注册","code":"20110"}},
                        {"data":{"mobilephone":"13821111114","pwd":"123456789009876543"},"expect":{"msg":"手机号码已被注册","code":"20110"}}
                        ])

def register_data(request):
    return request.param

def test_register(register_data):
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    print(r.json())
    print("测试数据:",register_data['data'])
    print("预期结果:",register_data['expect'])
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']
