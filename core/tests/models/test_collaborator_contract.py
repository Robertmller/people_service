import requests


# Testing collaborator_contract_contract
class Testcollaborator_contract_contracts:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_collaborator_contract = 'http://0.0.0.0:8000/api/v1/collaborator-contract/'

    def test_get_all_collaborator_contract_contracts(self):
        collaborator_contract_contracts = requests.get(
            url=self.url_base_collaborator_contract, headers=self.headers)

        assert collaborator_contract_contracts.status_code == 200

    def test_get_collaborator_contract(self):
        collaborator_contract = requests.get(
            url=f'{self.url_base_collaborator_contract}4/', headers=self.headers)

        assert collaborator_contract.status_code == 200

    def test_post_collaborator_contract(self):
        new_collaborator_contract = {
            "status": 0,
            "collaborator_id": 12,
            "contract_id": 13
        }
        result = requests.post(
            url=self.url_base_collaborator_contract, headers=self.headers, data=new_collaborator_contract)

        assert result.status_code == 201

    def test_put_collaborator_contract(self):
        update_collaborator_contract = {
            "status": -1679,
        }
        result = requests.put(
            url=f'{self.url_base_collaborator_contract}3/', headers=self.headers, data=update_collaborator_contract)

        assert result.status_code == 200

    def test_delete_collaborator_contract(self):
        result = requests.delete(
            url=f'{self.url_base_collaborator_contract}2/', headers=self.headers)

        assert result.status_code == 204
