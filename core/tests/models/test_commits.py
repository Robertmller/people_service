import requests


# Testing Commit
class TestCommits:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Commit = 'http://0.0.0.0:8000/api/v1/commits/'

    def test_get_all_Commits(self):
        Commits = requests.get(
            url=self.url_base_Commit, headers=self.headers)

        assert Commits.status_code == 200

    def test_get_Commit(self):
        Commit = requests.get(
            url=f'{self.url_base_Commit}8/', headers=self.headers)

        assert Commit.status_code == 200

    def test_post_Commit(self):
        new_Commit = {
            "description": "Teste T",
            "date_time": "2022-04-02T21:50:03.630Z",
            "task_repository_id": 10,
            "collaborator_id": 11
        }
        result = requests.post(
            url=self.url_base_Commit, headers=self.headers, data=new_Commit)

        assert result.status_code == 201

    def test_put_Commit(self):
        update_Commit = {
            "description": "New P",
            "date_time": "2024-03-02T02:43:48.620Z",
            "task_repository_id": 3
        }
        result = requests.put(
            url=f'{self.url_base_Commit}3/', headers=self.headers, data=update_Commit)

        assert result.status_code == 200

    def test_delete_Commit(self):
        result = requests.delete(
            url=f'{self.url_base_Commit}2/', headers=self.headers)

        assert result.status_code == 204
