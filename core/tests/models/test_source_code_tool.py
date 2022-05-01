import requests


# Testing Source_Code_Tool
class TestSource_Code_Tools:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Source_Code_Tool = 'http://0.0.0.0:8000/api/v1/source-code-tool/'

    def test_get_all_Source_Code_Tools(self):
        Source_Code_Tools = requests.get(
            url=self.url_base_Source_Code_Tool, headers=self.headers)

        assert Source_Code_Tools.status_code == 200

    def test_get_Source_Code_Tool(self):
        Source_Code_Tool = requests.get(
            url=f'{self.url_base_Source_Code_Tool}5/', headers=self.headers)

        assert Source_Code_Tool.status_code == 200

    def test_post_Source_Code_Tool(self):
        new_Source_Code_Tool = {
            "name": "robert_teste3",

        }
        result = requests.post(
            url=self.url_base_Source_Code_Tool, headers=self.headers, data=new_Source_Code_Tool)

        assert result.status_code == 201
        assert result.json()['name'] == new_Source_Code_Tool["name"]

    def test_put_Source_Code_Tool(self):
        update_Source_Code_Tool = {
            "name": "robert_muller8",

        }
        result = requests.put(
            url=f'{self.url_base_Source_Code_Tool}4/', headers=self.headers, data=update_Source_Code_Tool)

        assert result.status_code == 200
        assert result.json()['name'] == update_Source_Code_Tool["name"]

    def test_delete_Source_Code_Tool(self):
        result = requests.delete(
            url=f'{self.url_base_Source_Code_Tool}3/', headers=self.headers)

        assert result.status_code == 204
