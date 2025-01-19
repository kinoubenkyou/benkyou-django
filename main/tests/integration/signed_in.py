from main.tests.integration import DriverTestCase


class SignedInTestCase(DriverTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.web_driver.get(f"{cls.live_server_url}/")
        cls.web_driver.add_cookie({
            "domain": "localhost",
            "expiry": 32503680000,
            "httpOnly": True,
            "name": "sessionid",
            "path": "/",
            "sameSite": "Lax",
            "secure": False,
            "value": "ql2ne8u2de4hyfsgor3uzrz9tzy2ufkv",
        })
        cls.web_driver.add_cookie({
            "domain": "localhost",
            "expiry": 32503680000,
            "httpOnly": False,
            "name": "csrftoken",
            "path": "/",
            "sameSite": "Lax",
            "secure": False,
            "value": "NFTyv3rmdWcdioQLeR8Wwaz2YUeoPEA9",
        })
