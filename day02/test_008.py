import pytest
import requests

proxy = {
    "http": "http://127.0.0.1:8888"
}


@pytest.fixture(params=[
    {"data": {"mobilephone": '15912702547', "pwd": "123456789123456789"},
     "expect": {"msg": "手机号码已被注册", "code": "20110"}},
    {"data": {"mobilephone": '1345478581', "pwd": "123456"},
     "expect": {"msg": "手机号码格式不正确", "code": "20109"}},
    {"data": {"mobilephone": '13156782375', "pwd": "123"},
     "expect": {"msg": "密码长度必须为6~18", "code": "20108"}}])
def register_data(request):  # 参数request是固定的,不能写成其他
    return request.param  # 使用request.param返回每组数据


def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    r = requests.get(url, params=register_data['data'], proxies=proxy)
    assert r.json()['msg'] == register_data['expect']['msg']
    assert r.json()['code'] == register_data['expect']['code']
    print("实际结果:", r.json())
    print("测试数据:", register_data['data'])
    print("预期结果:", register_data['expect'])
