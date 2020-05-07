import requests

from test_requests.test_zuoye.api.base_api import BaseApi


class WeWorkt(BaseApi):
    corpid = "wwe99718602b3a2e7c"

    @classmethod
    def get_token(cls, secrete):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,
                         params={
                             "corpid": cls.corpid,
                             "corpsecret": secrete
                         })
        # corpid前加cls是因为调取类以外的值，secrete不带是因为调取内部值
        return r.json()["access_token"]