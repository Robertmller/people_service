import requests


# Testing repository
class Test_repositories:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_repository = 'http://0.0.0.0:8000/api/v1/repository/'

    def test_get_all_repositories(self):
        repositories = requests.get(
            url=self.url_base_repository, headers=self.headers)

        assert repositories.status_code == 200

    def test_get_repository(self):
        repository = requests.get(
            url=f'{self.url_base_repository}4/', headers=self.headers)

        assert repository.status_code == 200

    def test_post_repository(self):
        new_repository = {
            "link": "http://0.0.0.0:8000/api/v1",
            "ssh_link": "http://0.0.0.0:8000/api/v1",
            "project_id": 16
        }
        result = requests.post(
            url=self.url_base_repository, headers=self.headers, data=new_repository)

        assert result.status_code == 201

    def test_put_repository(self):
        update_repository = {
            "link": "http://0.0.0.0:8000/api/v1/repository/",
            "ssh_link": "http://0.0.0.0:8000/api/v1/repository/",
            "project_id": 5
        }
        result = requests.put(
            url=f'{self.url_base_repository}6/', headers=self.headers, data=update_repository)

        assert result.status_code == 200

    def test_delete_repository(self):
        result = requests.delete(
            url=f'{self.url_base_repository}9/', headers=self.headers)

        assert result.status_code == 204
