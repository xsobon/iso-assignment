"""
unit tests for whole app
"""
import unittest
import main
import json

input_no_count = {"iso": "svk",
                  "countries": []}

input_no_key = {"iso": "svk"}

input_blank = {}

input_wrong_word = {"iso": "pol",
                    "countries": [
                        "iran",
                        "Polonia",
                        "Slowakei",
                        "Ajdnfkruu"
                    ]}

exp_out_wrong_word = {"iso": "pol",
                      "match_count": 1,
                      "matches": [
                          "Polonia"
                      ]}

input_random_chars = {"iso": "deu",
                      "countries": [
                          "85642",
                          "  84 ul:'",
                          "Slowakei",
                          "Ujerumani",
                          "fg##996",
                          "  odk'%^*(("
                      ]}

exp_out_random_chars = {"iso": "deu",
                        "match_count": 1,
                        "matches": [
                            "Ujerumani"
                        ]}

input_wrong_iso = {"iso": "krk",
                   "countries": [
                       "Slovakia",
                       "Czechia",
                       "Poland"
                   ]}

input_wrong_iso2 = {"iso": "lk",
                    "countries": [
                        "Slovakia",
                        "Czechia",
                        "Poland"
                    ]}


input_easy_1 = {"iso": "svk",
                "countries": [
                    "Slovakia",
                    "Czechia",
                    "Poland"
                ]}

exp_out_easy_1 = {"iso": "svk",
                  "match_count": 1,
                  "matches": [
                      "Slovakia"
                  ]}

input_easy_2 = {"iso": "svk",
                "countries": [
                    "iran",
                    "Slowakei",
                    "Vatikan",
                    "Slovaška",
                    "Szlovákia",
                    "Belgrade",
                    "España",
                    "Nizozemsko"
                ]}

exp_out_easy_2 = {"iso": "svk",
                  "match_count": 3,
                  "matches": [
                      "Slowakei",
                      "Slovaška",
                      "Szlovákia"
                  ]}

input_easy_3 = {"iso": "dnk",
                "countries": [
                    "Tanska",
                    "Vatikan",
                    "Slovaška",
                    "Germany",
                    "Danska",
                    "Dinamarca",
                    "Dánsko"
                ]}

exp_out_easy_3 = {"iso": "dnk",
                  "match_count": 4,
                  "matches": [
                      "Tanska",
                      "Danska",
                      "Dinamarca",
                      "Dánsko"
                  ]}




class My_app_tests(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        self.app = main.app.test_client()

    def test_no_countries(self):
        res = self.app.post("/iso", data=input_no_count)
        assert 400 == res.status_code
        assert b"Without countries list there can't be any match." in res.data

    def test_no_key(self):
        res = self.app.post("/iso", data=input_no_key)
        assert 400 == res.status_code
        assert b"Without countries list there can't be any match." in res.data

    def test_blank(self):
        res = self.app.post("/iso", data=input_blank)
        assert 400 == res.status_code
        assert b"Add iso value." in res.data


    def test_wrong_word(self):
        res = self.app.post("/iso", data=input_wrong_word)
        assert 200 == res.status_code
        self.assertDictEqual(exp_out_wrong_word, json.loads(res.json))

    def test_random_chars(self):
        res = self.app.post("/iso", data=input_random_chars)
        assert 200 == res.status_code
        self.assertDictEqual(exp_out_random_chars, json.loads(res.json))

    def test_wrong_iso(self):
        res = self.app.post("/iso", data=input_wrong_iso)
        assert 400 == res.status_code
        assert b"Non existing ISO code" in res.data

    def test_wrong_iso2(self):
        res = self.app.post("/iso", data=input_wrong_iso2)
        assert 400 == res.status_code
        assert b"ISO code in wrong format." in res.data

    def test_easy_1(self):
        res = self.app.post("/iso", data=input_easy_1)
        #print(json.dumps(str(res.data), sort_keys=True))
        assert 200 == res.status_code
        self.assertDictEqual(exp_out_easy_1, json.loads(res.json))

    def test_easy_2(self):
        res = self.app.post("/iso", data=input_easy_2)
        assert 200 == res.status_code
        self.assertDictEqual(exp_out_easy_2, json.loads(res.json))

    def test_easy_3(self):
        res = self.app.post("/iso", data=input_easy_3)
        assert 200 == res.status_code
        self.assertDictEqual(exp_out_easy_3, json.loads(res.json))




if __name__ == '__main__':
    unittest.main()




