import requests


# Testing Status_Project
class TestStatus_Projects:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Status_Project = 'http://0.0.0.0:8000/api/v1/status-project/'

    def test_get_all_Status_Projects(self):
        Status_Projects = requests.get(
            url=self.url_base_Status_Project, headers=self.headers)

        assert Status_Projects.status_code == 200

    def test_get_Status_Project(self):
        Status_Project = requests.get(
            url=f'{self.url_base_Status_Project}3/', headers=self.headers)

        assert Status_Project.status_code == 200

    def test_post_Status_Project(self):
        new_Status_Project = {
            "name": "robert_teste11",

        }
        result = requests.post(
            url=self.url_base_Status_Project, headers=self.headers, data=new_Status_Project)

        assert result.status_code == 201
        assert result.json()['name'] == new_Status_Project["name"]

    def test_put_Status_Project(self):
        update_Status_Project = {
            "name": "robert_muller22",

        }
        result = requests.put(
            url=f'{self.url_base_Status_Project}7/', headers=self.headers, data=update_Status_Project)

        assert result.status_code == 200
        assert result.json()['name'] == update_Status_Project["name"]

    def test_delete_Status_Project(self):
        result = requests.delete(
            url=f'{self.url_base_Status_Project}5/', headers=self.headers)

        assert result.status_code == 204
