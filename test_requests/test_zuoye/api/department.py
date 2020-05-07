import requests

from test_requests.test_zuoye.api.weworkt import WeWorkt


class Department(WeWorkt):
    secrete = "aEOKRsyRLO4H8ETeLk2RawUW8IzAIAl2jW6N9T0TcPk"

    def create(self, name, parentid, **kwargs):
        data = {"name": name, "parentid": parentid}
        data.update(kwargs)

        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        r = requests.post(url,
                          params={
                              "access_token": WeWorkt.get_token(self.secrete)
                          },
                          json=data
                          )
        return r.json()

    def update(self, id, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {"id": id}
        data.update(kwargs)
        r = requests.post(url,
                          params={
                              "access_token": WeWorkt.get_token(self.secrete)},
                          json=data
                          )
        return r.json()

    def delete(self, id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(url, params={"access_token": WeWorkt.get_token(self.secrete),
                                      "id": id})
        return r.json()

    def get(self, id):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(url,
                         params={"access_token": WeWorkt.get_token(self.secrete),
                                 "id": id})
        return r.json()

