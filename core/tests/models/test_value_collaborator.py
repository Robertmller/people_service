import requests


# Testing value_collaborator
class TestValue_Collaborators:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_value_collaborator = 'http://0.0.0.0:8000/api/v1/value-collaborator/'

    def test_get_all_value_collaborators(self):
        value_collaborators = requests.get(
            url=self.url_base_value_collaborator, headers=self.headers)

        assert value_collaborators.status_code == 200

    def test_get_value_collaborator(self):
        value_collaborator = requests.get(
            url=f'{self.url_base_value_collaborator}9/', headers=self.headers)

        assert value_collaborator.status_code == 200

    def test_post_value_collaborator(self):
        new_value_collaborator = {
            "value": 1000,
            "date_end": "2022-08-02",
            "collaborator_id": 17
        }
        result = requests.post(
            url=self.url_base_value_collaborator, headers=self.headers, data=new_value_collaborator)

        assert result.status_code == 201

    def test_put_value_collaborator(self):
        update_value_collaborator = {
            "value": 999,
            "date_end": "2022-03-02",
            "collaborator_id": 12
        }

        result = requests.put(
            url=f'{self.url_base_value_collaborator}7/', headers=self.headers, data=update_value_collaborator)

        assert result.status_code == 200

    def test_delete_value_collaborator(self):
        result = requests.delete(
            url=f'{self.url_base_value_collaborator}5/', headers=self.headers)

        assert result.status_code == 204
