import json


class BaseApi:
    @classmethod
    def format(cls, r):
        print(json.dumps(r.json(), indent=2))
