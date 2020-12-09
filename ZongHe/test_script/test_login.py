'''
登录接口测试脚本
'''
import pytest

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead


@pytest.fixture(params=DataRead.read_yaml("data_case/login_setup.yaml"),scope='module')
def setup_data(request):
    return request.param


@pytest.fixture(params=DataRead.read_yaml("data_case/login_data.yaml"))
def login_data(request):
    return request.param

@pytest.fixture(scope='module')
def register(setup_data, url, db, baserequests):
    # 注册用户
    print(f"测试数据:{setup_data}")
    mobile = setup_data['casedata']['mobilephone']
    # 下发注册请求
    r = Member.register(url, baserequests, setup_data['casedata'])
    yield
    # 删除注册用户
    DbOp.delete_user(db, mobile)


def test_login(register, login_data, url, baserequests):
    # 下发登录的请求
    r = Member.login(url, baserequests, login_data['casedata'])
    # 检查结果
    print(r.json())
    assert r.json()['msg'] == login_data['expect']['msg']
    assert r.json()['code'] == login_data['expect']['code']
