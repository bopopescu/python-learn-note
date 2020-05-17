import unittest
from pprint import pprint
from question_4 import judge_pass, judge_pass_with_re

class TestPassword(unittest.TestCase):

    def setUp(self):
        self.password_list = [
            {
                "password": "12344567",
                "want": 'very weak'
            },
            {
                "password": "dsdfsd",
                "want": "very weak"
            },
            {
                "password": "(*&%%*&)",
                "want": "very weak"
            },
            {
                "password": "123sdfsf",
                "want": "weak",
            },
            {
                "password": "*&12&*&",
                "want": "weak"
            },
            {
                "password": "asdf&%$",
                "want": "weak"
            },
            {
                "password": "MNTD&%$",
                "want": "weak"
            },
            {
                "password": "aMNTD&%$",
                "want": "medium"
            },
            {
                "password": "aMNTD123",
                "want": "medium"
            },
            {
                "password": "aMNTD12&",
                "want": "strong"
            },
            {
                "password": "aMNTD123&sdf",
                "want": "very strong"
            },
            {
                "password": "aMN",
                "want": "invalid"
            },
        ]
        print("prepare data: ")
        pprint(self.password_list)
        print("*" * 100)
    
    def test_password_without_re(self):
        print('test password without re')
        for data in self.password_list:
            res = judge_pass(data.get("password"))
            print("password: {}, got: {}, want: "
                  "{}".format(data.get("password"), res, data.get("want")))
            assert res == data.get('want')

    def test_password_with_re(self):
        print('test password with re')
        for data in self.password_list:
            res = judge_pass_with_re(data.get("password"))
            print("password: {}, got: {}, want: "
                  "{}".format(data.get("password"), res, data.get("want")))
            assert res == data.get('want')
    

if __name__ == "__main__":
    unittest.main()
