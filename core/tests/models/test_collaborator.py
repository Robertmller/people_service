import requests


# Testing collaborator
class Test_Collaborators:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_collaborator = 'http://0.0.0.0:8000/api/v1/collaborator/'

    def test_get_all_collaborators(self):
        collaborators = requests.get(
            url=self.url_base_collaborator, headers=self.headers)

        assert collaborators.status_code == 200

    def test_get_collaborator(self):
        collaborator = requests.get(
            url=f'{self.url_base_collaborator}13/', headers=self.headers)

        assert collaborator.status_code == 200

    def test_post_collaborator(self):
        new_collaborator = {
            "name": "Test",
            "cpf": "99999999",
            "cnpj": "12222222222",
            "rg": "9990000000",
            "born_date": "2022-03-04",
            "areopagus_business_id": 8,
            "type_id": 14
        }
        result = requests.post(
            url=self.url_base_collaborator, headers=self.headers, data=new_collaborator)

        assert result.status_code == 201
        assert result.json()['name'] == new_collaborator["name"]

    def test_put_collaborator(self):
        update_collaborator = {
            "name": "Loremm",

        }
        result = requests.put(
            url=f'{self.url_base_collaborator}8/', headers=self.headers, data=update_collaborator)

        assert result.status_code == 200
        assert result.json()['name'] == update_collaborator["name"]

    def test_delete_collaborator(self):
        result = requests.delete(
            url=f'{self.url_base_collaborator}4/', headers=self.headers)

        assert result.status_code == 204
