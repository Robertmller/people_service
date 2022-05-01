import requests


# Testing Status_Task
class TestStatus_Tasks:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Status_Task = 'http://0.0.0.0:8000/api/v1/status-task/'

    def test_get_all_Status_Tasks(self):
        Status_Tasks = requests.get(
            url=self.url_base_Status_Task, headers=self.headers)

        assert Status_Tasks.status_code == 200

    def test_get_Status_Task(self):
        Status_Task = requests.get(
            url=f'{self.url_base_Status_Task}6/', headers=self.headers)

        assert Status_Task.status_code == 200

    def test_post_Status_Task(self):
        new_Status_Task = {
            "name": "robert_teste14",

        }
        result = requests.post(
            url=self.url_base_Status_Task, headers=self.headers, data=new_Status_Task)

        assert result.status_code == 201
        assert result.json()['name'] == new_Status_Task["name"]

    def test_put_Status_Task(self):
        update_Status_Task = {
            "name": "robert_muller66",

        }
        result = requests.put(
            url=f'{self.url_base_Status_Task}5/', headers=self.headers, data=update_Status_Task)

        assert result.status_code == 200
        assert result.json()['name'] == update_Status_Task["name"]

    def test_delete_Status_Task(self):
        result = requests.delete(
            url=f'{self.url_base_Status_Task}4/', headers=self.headers)

        assert result.status_code == 204
