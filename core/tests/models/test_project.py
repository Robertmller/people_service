import requests


# Testing project
class Test_projects:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_project = 'http://0.0.0.0:8000/api/v1/project/'

    def test_get_all_projects(self):
        projects = requests.get(
            url=self.url_base_project, headers=self.headers)

        assert projects.status_code == 200

    def test_get_project(self):
        project = requests.get(
            url=f'{self.url_base_project}5/', headers=self.headers)

        assert project.status_code == 200

    def test_post_project(self):
        new_project = {
            "name": "stringsss",
            "documentaion_id": 5,
            "doc_link": "string",
            "contract_id": 14,
            "status_project_id": 9
        }
        result = requests.post(
            url=self.url_base_project, headers=self.headers, data=new_project)

        assert result.status_code == 201

    def test_put_project(self):
        update_project = {
            "name": "Lorem Ipsumssss",
            "documentaion_id": 7,
            "doc_link": "http://0.0.0.0:8000/api/v1/project/",
            "contract_id": 2,
            "status_project_id": 3
        }
        result = requests.put(
            url=f'{self.url_base_project}3/', headers=self.headers, data=update_project)

        assert result.status_code == 200

    def test_delete_project(self):
        result = requests.delete(
            url=f'{self.url_base_project}4/', headers=self.headers)

        assert result.status_code == 204
