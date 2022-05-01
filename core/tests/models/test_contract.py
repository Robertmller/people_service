import requests


# Testing project
class Test_projects:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_project = 'http://0.0.0.0:8000/api/v1/contract/'

    def test_get_all_projects(self):
        projects = requests.get(
            url=self.url_base_project, headers=self.headers)

        assert projects.status_code == 200

    def test_get_project(self):
        project = requests.get(
            url=f'{self.url_base_project}6/', headers=self.headers)

        assert project.status_code == 200

    def test_post_project(self):
        new_project = {
            "cnpj": "9999999555999",
            "playlist_link": "http://0.0.0.0:8000/api/v1/contract/",
            "meet_id": 3,
            "tech_lead_name": "string",
            "coorporative_email": "string",
            "begin_date_contract": "2022-05-02",
            "date_end_contract": "2022-03-07",
            "hours_control_link": "http://0.0.0.0:8000/api/v1/contract/",
            "is_full_time": True,
            "is_international": True,
            "value": 1000,
            "communication_tool_id": 17,
            "estate_id": 16,
            "status_contract_id": 4
        }
        result = requests.post(
            url=self.url_base_project, headers=self.headers, data=new_project)

        assert result.status_code == 201

    def test_put_project(self):
        update_project = {
            "cnpj": "888444488888",
            "playlist_link": "http://0.0.0.0:8000/api/v1/contract/",
            "tech_lead_name": "string",
            "coorporative_email": "string",
            "value": 3330,
        }
        result = requests.put(
            url=f'{self.url_base_project}5/', headers=self.headers, data=update_project)

        assert result.status_code == 200

    def test_delete_project(self):
        result = requests.delete(
            url=f'{self.url_base_project}4/', headers=self.headers)

        assert result.status_code == 204
