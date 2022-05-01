import requests


# Testing task_tool_contract
class Testtask_tool_contracts:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_task_tool_contract = 'http://0.0.0.0:8000/api/v1/task-tool-contract/'

    def test_get_all_task_tool_contracts(self):
        task_tool_contracts = requests.get(
            url=self.url_base_task_tool_contract, headers=self.headers)

        assert task_tool_contracts.status_code == 200

    def test_get_task_tool_contract(self):
        task_tool_contract = requests.get(
            url=f'{self.url_base_task_tool_contract}7/', headers=self.headers)

        assert task_tool_contract.status_code == 200

    def test_post_task_tool_contract(self):
        new_task_tool_contract = {
            "link": "http://0.0.0.0:8000/api/v1/task-tool-contract/",
            "contract_id": 8,
            "task_tool_id": 9
        }
        result = requests.post(
            url=self.url_base_task_tool_contract, headers=self.headers, data=new_task_tool_contract)

        assert result.status_code == 201

    def test_put_task_tool_contract(self):
        update_task_tool_contract = {
            "link": "strissssng",
            "contract_id": 4,
            "task_tool_id": 5
        }
        result = requests.put(
            url=f'{self.url_base_task_tool_contract}5/', headers=self.headers, data=update_task_tool_contract)

        assert result.status_code == 200

    def test_delete_task_tool_contract(self):
        result = requests.delete(
            url=f'{self.url_base_task_tool_contract}3/', headers=self.headers)

        assert result.status_code == 204
