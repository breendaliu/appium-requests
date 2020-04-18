# 获取客户群列表，获取客户群详情封装在这个文件中

import json

import requests


class GroupChat:
    def list(self, token, offset=1, limit=10, **kwargs):
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
            params={"access_token": token},
            json=data
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def get(self, chat_id, token):
        detail_url = "https://qyapi.weixin.qq.com/cgi-bin/externalcontact/groupchat/get"
        r = requests.post(
            detail_url,
            params={"access_token": token},
            json={"chat_id": chat_id}
        )
        # 打印出格式化后的json
        print(json.dumps(r.json(), indent=2))
        return r.json()