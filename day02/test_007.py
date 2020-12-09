'''
fixture带参数
'''
import pytest

# 测试数据
# 参数使用params关键字,一个列表,列表中有3组数据,每组数据是个字典.
@pytest.fixture(params=[{"username": "root", "pwd": "123456"},
                        {"username": "admin", "pwd": "888888"},
                        {"username": "administrator", "pwd": "HelloPwd"},
                        "foue",
                        5])
def login_data(request):  # 参数request是固定的,不能写成其他
    return request.param  # 使用request.param返回每组数据

# 测试逻辑(测试步骤)
# 登录功能的测试脚本
def test_login(login_data):
    print(f"测试登录成功,测试数据为:{login_data}")


