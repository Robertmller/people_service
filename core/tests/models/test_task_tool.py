import requests


# Testing Task_Tool
class TestTask_Tools:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Task_Tool = 'http://0.0.0.0:8000/api/v1/task-tool/'

    def test_get_all_Task_Tools(self):
        Task_Tools = requests.get(
            url=self.url_base_Task_Tool, headers=self.headers)

        assert Task_Tools.status_code == 200

    def test_get_Task_Tool(self):
        Task_Tool = requests.get(
            url=f'{self.url_base_Task_Tool}6/', headers=self.headers)

        assert Task_Tool.status_code == 200

    def test_post_Task_Tool(self):
        new_Task_Tool = {
            "name": "robert_teste1",

        }
        result = requests.post(
            url=self.url_base_Task_Tool, headers=self.headers, data=new_Task_Tool)

        assert result.status_code == 201
        assert result.json()['name'] == new_Task_Tool["name"]

    def test_put_Task_Tool(self):
        update_Task_Tool = {
            "name": "robert_muller",

        }
        result = requests.put(
            url=f'{self.url_base_Task_Tool}5/', headers=self.headers, data=update_Task_Tool)

        assert result.status_code == 200
        assert result.json()['name'] == update_Task_Tool["name"]

    def test_delete_Task_Tool(self):
        result = requests.delete(
            url=f'{self.url_base_Task_Tool}3/', headers=self.headers)

        assert result.status_code == 204
