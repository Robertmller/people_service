import requests


# Testing Justify
class TestJustifies:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_Justify = 'http://0.0.0.0:8000/api/v1/justify/'

    def test_get_all_Justifies(self):
        Justifies = requests.get(
            url=self.url_base_Justify, headers=self.headers)

        assert Justifies.status_code == 200

    def test_get_Justify(self):
        Justify = requests.get(
            url=f'{self.url_base_Justify}6/', headers=self.headers)

        assert Justify.status_code == 200

    def test_post_Justify(self):
        new_Justify = {
            "description": "stringss",
            "date_time": "2022-05-02",
            "collaborator_id": 11
        }
        result = requests.post(
            url=self.url_base_Justify, headers=self.headers, data=new_Justify)

        assert result.status_code == 201

    def test_put_Justify(self):
        update_Justify = {
            "description": "Teste Ipsummmm",
            "date_time": "2022-03-08"
        }
        result = requests.put(
            url=f'{self.url_base_Justify}5/', headers=self.headers, data=update_Justify)

        assert result.status_code == 200

    def test_delete_Justify(self):
        result = requests.delete(
            url=f'{self.url_base_Justify}4/', headers=self.headers)

        assert result.status_code == 204
