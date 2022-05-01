import requests


# Testing Status_Contract
class TestStatus_Contracts:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Status_Contract = 'http://0.0.0.0:8000/api/v1/status-contract/'

    def test_get_all_Status_Contracts(self):
        Status_Contracts = requests.get(
            url=self.url_base_Status_Contract, headers=self.headers)

        assert Status_Contracts.status_code == 200

    def test_get_Status_Contract(self):
        Status_Contract = requests.get(
            url=f'{self.url_base_Status_Contract}8/', headers=self.headers)

        assert Status_Contract.status_code == 200

    def test_post_Status_Contract(self):
        new_Status_Contract = {
            "name": "robert_teste5",

        }
        result = requests.post(
            url=self.url_base_Status_Contract, headers=self.headers, data=new_Status_Contract)

        assert result.status_code == 201
        assert result.json()['name'] == new_Status_Contract["name"]

    def test_put_Status_Contract(self):
        update_Status_Contract = {
            "name": "robert_muller9",

        }
        result = requests.put(
            url=f'{self.url_base_Status_Contract}7/', headers=self.headers, data=update_Status_Contract)

        assert result.status_code == 200
        assert result.json()['name'] == update_Status_Contract["name"]

    def test_delete_Status_Contract(self):
        result = requests.delete(
            url=f'{self.url_base_Status_Contract}4/', headers=self.headers)

        assert result.status_code == 204
