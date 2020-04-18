import json

import requests

from test_requests.test_wework.groupchat import GroupChat
from test_requests.test_wework.wework import WeWork


class TestWeWork:
    test_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid="wwe99718602b3a2e7c"
    # 应用管理test的secret, def test_get_token使用
    # secret="K4FB34TpHj7sFPTnnL0KF6n13r-V6eRGKNbGVOXhiio"
    # 客户联系->客户的secret，def test_groupchat_detail使用
    secret="TzYDZdObJKUvRm1WiI8c6Znk3rYEGYRPHw400nvELgg"
    # 未获取到token时，先赋给一个空值
    token=None

    #类的装饰器
    @classmethod
    # 设定一个类方法，获取token值，每次运行调取新的token
    # cls代表的是类
    def setup_class(cls):
        # 创建群聊对象，引入GroupChat
        cls.groupchat=GroupChat()
        # 创建全局变量token用例，从中调取token
        cls.token=WeWork.get_token(cls.secret)

    # 获取token
    def test_get_token(self):
        r=WeWork.get_access_token(self.secret)
        assert r["errcode"] == 0

    # 验证token是否获取到
    def test_get_token_exist(self):
        assert self.token is not None

    # 接口：外部联系人管理-》客户群管理-》获取客户群列表，调用groupchat封装的客户群列表用例，并传入参数，进行测试
    def test_groupchat_get(self):
        # r = self.groupchat.list(offset=0, limit=10, token=self.token)
        # 导入groupchat下的list, 由于设置了offset=0, limit=10的默认值，所以传入的参数中不需要再填写
        r = self.groupchat.list(token=self.token)
        assert r["errcode"]==0

    # 传入其他参数，status_filter=1
    def test_groupchat_get_status(self):
        r = self.groupchat.list(token=self.token, offset=0, limit=10, status_filter=1)
        assert r["errcode"] == 0

    # 接口：外部联系人管理-》客户群管理-》获取客户群详情，调用groupchat封装的客户群群详细信息用例，并传入参数，进行测试
    def test_groupchat_detail(self):
        r = self.groupchat.list(token=self.token)
        assert r["errcode"]==0

        chat_id = r["group_chat_list"][0]["chat_id"]
        r = self.groupchat.get(chat_id, self.token)
        assert r["errcode"] == 0
        assert len(r["group_chat"]["member_list"]) > 0

