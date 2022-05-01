import requests


# Testing Type
class TestTypes:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_type = 'http://0.0.0.0:8000/api/v1/communication-tool/'

    def test_get_all_types(self):
        types = requests.get(
            url=self.url_base_type, headers=self.headers)

        assert types.status_code == 200

    def test_get_type(self):
        type = requests.get(
            url=f'{self.url_base_type}6/', headers=self.headers)

        assert type.status_code == 200

    def test_post_type(self):
        new_type = {
            "name": "robert_teste1",

        }
        result = requests.post(
            url=self.url_base_type, headers=self.headers, data=new_type)

        assert result.status_code == 201
        assert result.json()['name'] == new_type["name"]

    def test_put_type(self):
        update_type = {
            "name": "robert_muller1",

        }
        result = requests.put(
            url=f'{self.url_base_type}5/', headers=self.headers, data=update_type)

        assert result.status_code == 200
        assert result.json()['name'] == update_type["name"]

    def test_delete_type(self):
        result = requests.delete(
            url=f'{self.url_base_type}4/', headers=self.headers)

        assert result.status_code == 204
