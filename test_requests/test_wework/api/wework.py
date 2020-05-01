# token放在更全局的变量中
import json

import requests

from test_requests.test_wework.api.baseapi import BaseApi


class WeWork(BaseApi):
    test_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
    corpid = "wwe99718602b3a2e7c"
    # 每个接口token不一样，所以需要定义成一个词典
    token = dict()
    secret = "TzYDZdObJKUvRm1WiI8c6Znk3rYEGYRPHw400nvELgg"

    @classmethod
    def get_token(cls, secret=secret):
        if secret is None:
            return cls.token[secret]
        # 如果密钥secret不在token值中，则重新获取。如果存在，则直接返回。避免重复请求，提高速度
        if secret not in cls.token.keys():
            r = cls.get_access_token(secret)
            # r.json是返回json体，取出json对象，取出json下的一个字段
            # assert r["errcode"] == 0
            # 存储token到变量token中
            cls.token[secret] = r["access_token"]
        return cls.token[secret]

    @classmethod
    def get_access_token(cls, secret):
        r = requests.get(
            cls.test_url,
            params={"corpid": cls.corpid, "corpsecret": secret}
        )
        cls.format(r)
        assert r.json()["errcode"] == 0
        return r.json()
