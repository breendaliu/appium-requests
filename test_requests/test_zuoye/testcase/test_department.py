from test_requests.test_zuoye.api.department import Department
from test_requests.test_zuoye.api.weworkt import WeWorkt


class TestDeparement:
    def setup(self):
        self.department = Department()

    def test_token(self):
        r = WeWorkt.get_token("aEOKRsyRLO4H8ETeLk2RawUW8IzAIAl2jW6N9T0TcPk")
        assert r["errcode"] == 0

    def test_create(self):
        r = self.department.create("may", 1)
        assert r["errcode"] == 0

    def test_update(self):
        r = self.department.update(3, name="abcd")
        assert r["errmsg"] == "updated"

    def test_delete(self):
        r = self.department.delete(3)
        assert r["errmsg"] == "deleted"

    def test_get(self):
        r = self.department.get(3)
        print(r)
        assert r["errmsg"] == "ok"


