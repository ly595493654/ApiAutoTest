'''
Member模块的接口
'''


def register(url, baserequests, data):
    '''
    注册接口
    :param url:  环境信息,比如 http://jy001:8081/
    :param baserequests:   baserequests的实例
    :param data:  注册的测试数据
    :return:  相应信息
    '''
    url = url + "futureloan/mvc/api/member/register"
    r = baserequests.post(url, data=data)
    return r


def list(url, baserequests):
    url = url + "futureloan/mvc/api/member/list"
    r = baserequests.get(url)
    return r


def login(url, baserequests, data):
    url = url + "futureloan/mvc/api/member/login"
    r = baserequests.post(url, data=data)
    return r


if __name__ == '__main__':
    from ZongHe.caw.BaseRequests import BaseRequests

    b = BaseRequests()
    canshu = {"mobilephone": "18165403935", "pwd": "123456"}
    r = register("http://jy001:8081/", b, canshu)
    print(r.text)
