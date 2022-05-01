import requests


# Testing Estate
class TestEstaties:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_estate = 'http://0.0.0.0:8000/api/v1/estate/'

    def test_get_all_estaties(self):
        estaties = requests.get(
            url=self.url_base_estate, headers=self.headers)

        assert estaties.status_code == 200

    def test_get_estate(self):
        estate = requests.get(
            url=f'{self.url_base_estate}5/', headers=self.headers)

        assert estate.status_code == 200

    def test_post_estate(self):
        new_estate = {
            "name": "robert_teste2",

        }
        result = requests.post(
            url=self.url_base_estate, headers=self.headers, data=new_estate)

        assert result.status_code == 201
        assert result.json()['name'] == new_estate["name"]

    def test_put_estate(self):
        update_estate = {
            "name": "robert_muller6",

        }
        result = requests.put(
            url=f'{self.url_base_estate}4/', headers=self.headers, data=update_estate)

        assert result.status_code == 200
        assert result.json()['name'] == update_estate["name"]

    def test_delete_estate(self):
        result = requests.delete(
            url=f'{self.url_base_estate}3/', headers=self.headers)

        assert result.status_code == 204
