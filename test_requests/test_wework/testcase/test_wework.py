from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:
    # # 未获取到token时，先赋给一个空值
    # token=None

    #类的装饰器
    @classmethod
    # 设定一个类方法，获取token值，每次运行调取新的token
    # cls代表的是类
    def setup_class(cls):
        # 创建群聊对象，引入GroupChat
        cls.groupchat=GroupChat()
        # 创建全局变量token用例，从中调取token
        cls.token=WeWork.get_token()

    # 获取token
    def test_get_token(self):
        r=WeWork.get_access_token(WeWork.secret)
        assert r["errcode"] == 0

    # 验证token是否获取到
    def test_get_token_exist(self):
        assert self.token is not None
