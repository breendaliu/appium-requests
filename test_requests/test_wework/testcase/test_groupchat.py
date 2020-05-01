from test_requests.test_wework.api.groupchat import GroupChat
from test_requests.test_wework.api.wework import WeWork


class TestWeWork:
    # # 未获取到token时，先赋给一个空值
    # token=None

    # 类的装饰器
    @classmethod
    # 设定一个类方法，获取token值，每次运行调取新的token
    # cls代表的是类
    def setup_class(cls):
        # 创建群聊对象，引入GroupChat
        cls.groupchat = GroupChat()
        # 创建全局变量token用例，从中调取token
        # cls.token=WeWork.get_token(cls.groupchat.secret)

    # 接口：外部联系人管理-》客户群管理-》获取客户群列表，调用groupchat封装的客户群列表用例，并传入参数，进行测试
    def test_groupchat_get(self):
        # r = self.groupchat.list(offset=0, limit=10, token=self.token)
        # 导入groupchat下的list, 由于设置了offset=0, limit=10的默认值，所以传入的参数中不需要再填写
        r = self.groupchat.list()
        assert r["errcode"] == 0

    # 传入其他参数，status_filter=1
    def test_groupchat_get_status(self):
        r = self.groupchat.list(status_filter=1)
        assert r["errcode"] == 0

    # 接口：外部联系人管理-》客户群管理-》获取客户群详情，调用groupchat封装的客户群群详细信息用例，并传入参数，进行测试
    def test_groupchat_detail(self):
        r = self.groupchat.list(offset=0, limit=10)
        assert r["errcode"] == 0

        chat_id = r["group_chat_list"][0]["chat_id"]
        r = self.groupchat.get(chat_id)
        assert r["errcode"] == 0
        assert len(r["group_chat"]["member_list"]) > 0
