# 获取客户群列表，获取客户群详情封装在这个文件中

import json

import requests

from test_requests.test_wework.api.wework import WeWork


class GroupChat(WeWork):
    # 应用管理test的secret, def test_get_token使用
    # secret="K4FB34TpHj7sFPTnnL0KF6n13r-V6eRGKNbGVOXhiio"
    # 客户联系->客户的secret，def test_groupchat_detail使用
    secret = "TzYDZdObJKUvRm1WiI8c6Znk3rYEGYRPHw400nvELgg"

    def list(self, offset=1, limit=10, **kwargs):
        # **kwargs代表可传入其他参数
        # offset=1, limit=10为设定默认值，设定后，case中不需要再重新填写； 没有默认值的需要靠前，如token
        url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/list"
        data = {"offset": offset, "limit": limit}
        print(kwargs)
        print(data)
        data.update(kwargs)
        print(data)
        r = requests.post(
            url,
            params={"access_token": self.get_token(self.secret)},
            json=data
        )
        self.format(r)
        return r.json()

    def get(self, chat_id):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": self.get_token(self.secret)},
            json={"chat_id": chat_id}
        )
        # 打印出格式化后的json
        self.format(r)
        return r.json()
