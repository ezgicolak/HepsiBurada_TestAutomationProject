import unittest
import requests
import json


class Test(unittest.TestCase):

    def test_add_new_pet_post(self):
        api_url = "https://petstore.swagger.io/v2/pet"

        data = json.dumps({'id': 5, 'name': 'jane', 'status': 'sold'})
        resp = requests.post(api_url, data, headers={'accept': 'application/json', 'Content-Type': 'application/json'})
        print(resp)

    def test_fin_pet_by_ID_get(self):
        r = requests.get("https://petstore.swagger.io/v2/pet/5")
        print(r.json())
        print(r.status_code)

    def test_delete_pet(self):

        api_url = "https://petstore.swagger.io/v2/pet/5"
        resp = requests.delete(api_url)
        print(resp)

    def test_fin_pet_by_ID_get(self):
        r = requests.get("https://petstore.swagger.io/v2/pet/5")
        print(r.json())
        print(r.status_code)

if __name__ == "__main__":
    unittest.main()
