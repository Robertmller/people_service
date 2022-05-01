import requests


# Testing task_respository
class Test_Task_respositorys:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_task_respository = 'http://0.0.0.0:8000/api/v1/task-repository/'

    def test_get_all_task_respositories(self):
        task_respositories = requests.get(
            url=self.url_base_task_respository, headers=self.headers)

        assert task_respositories.status_code == 200

    def test_get_task_respository(self):
        task_respository = requests.get(
            url=f'{self.url_base_task_respository}5/', headers=self.headers)

        assert task_respository.status_code == 200

    def test_post_task_respository(self):
        new_task_respository = {
            "total_commits": 10,
            "task_id": 13,
            "repository_id": 12
        }
        result = requests.post(
            url=self.url_base_task_respository, headers=self.headers, data=new_task_respository)

        assert result.status_code == 201

    def test_put_task_respository(self):
        update_task_respository = {
            "total_commits": 8,
            "task_id": 6,
            "repository_id": 5
        }
        result = requests.put(
            url=f'{self.url_base_task_respository}4/', headers=self.headers, data=update_task_respository)

        assert result.status_code == 200

    def test_delete_task_respository(self):
        result = requests.delete(
            url=f'{self.url_base_task_respository}2/', headers=self.headers)

        assert result.status_code == 204
