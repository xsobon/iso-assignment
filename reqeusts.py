"""
testing conection for api
"""
import requests


input1 = {"iso": "cze",
         "countries": [
             "Slovakia",
             "Czechia",
             "Poland"
         ]}

input2 = {"iso": "svk",
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

input3 = {"iso": "hun",
          "countries": [
                "Italio",
                "Slowakei",
                "Belgie",
                "Magyarország",
                "Spanja",
                "l-ungerija",
                "España",
                "Ungarn "
            ]}





if __name__ == '__main__':

    Base_url = "http://127.0.0.1:5000/"

    response = requests.post(Base_url + "iso", input1)
    print(response.json())

    response = requests.post(Base_url + "iso", input2)
    print(response.json())

    response = requests.post(Base_url + "iso", input3)
    print(response.json())
