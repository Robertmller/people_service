import requests


# Testing source_code_tool_contract
class Test_source_code_tool_contracts:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_source_code_tool_contract = 'http://0.0.0.0:8000/api/v1/source-code-tool/'

    def test_get_all_source_code_tool_contracts(self):
        source_code_tool_contracts = requests.get(
            url=self.url_base_source_code_tool_contract, headers=self.headers)

        assert source_code_tool_contracts.status_code == 200

    def test_get_source_code_tool_contract(self):
        source_code_tool_contract = requests.get(
            url=f'{self.url_base_source_code_tool_contract}4/', headers=self.headers)

        assert source_code_tool_contract.status_code == 200

    def test_post_source_code_tool_contract(self):
        new_source_code_tool_contract = {
            "link": "string",
            "contract_id": 7,
            "source_code_tool_id": 8
        }
        result = requests.post(
            url=self.url_base_source_code_tool_contract, headers=self.headers, data=new_source_code_tool_contract)

        assert result.status_code == 201

    def test_put_source_code_tool_contract(self):
        update_source_code_tool_contract = {
            "name": "Robert Muller"
        }
        result = requests.put(
            url=f'{self.url_base_source_code_tool_contract}12/', headers=self.headers, data=update_source_code_tool_contract)

        assert result.status_code == 200

    def test_delete_source_code_tool_contract(self):
        result = requests.delete(
            url=f'{self.url_base_source_code_tool_contract}5/', headers=self.headers)

        assert result.status_code == 204
