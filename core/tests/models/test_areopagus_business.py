import requests


# Testing areopagus_business
class TestAreopagusBusiness:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_areopagus_business = 'http://0.0.0.0:8000/api/v1/areopagus-business/'

    def test_get_all_areopagus_business(self):
        areopagus_business = requests.get(
            url=self.url_base_areopagus_business, headers=self.headers)

        assert areopagus_business.status_code == 200

    def test_get_areopagus_business(self):
        areopagus_business = requests.get(
            url=f'{self.url_base_areopagus_business}4/', headers=self.headers)

        assert areopagus_business.status_code == 200

    def test_post_areopagus_business(self):
        new_areopagus_business = {
            "name": "robert_teste",
        }
        result = requests.post(
            url=self.url_base_areopagus_business, headers=self.headers, data=new_areopagus_business)

        assert result.status_code == 201
        assert result.json()['name'] == new_areopagus_business["name"]

    def test_put_areopagus_business(self):
        update_areopagus_business = {
            "name": "robert_muller",
        }
        result = requests.put(
            url=f'{self.url_base_areopagus_business}3/', headers=self.headers, data=update_areopagus_business)

        assert result.status_code == 200
        assert result.json()['name'] == update_areopagus_business["name"]

    def test_delete_areopagus_business(self):
        result = requests.delete(
            url=f'{self.url_base_areopagus_business}2', headers=self.headers)

        assert result.status_code == 204
