import requests


# Testing calendar
class TestCalendar:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_calendar = 'http://0.0.0.0:8000/api/v1/calendar/'

    def test_get_all_calendars(self):
        calendars = requests.get(
            url=self.url_base_calendar, headers=self.headers)

        assert calendars.status_code == 200

    def test_get_calendar(self):
        calendar = requests.get(
            url=f'{self.url_base_calendar}5/', headers=self.headers)

        assert calendar.status_code == 200

    def test_post_calendar(self):
        new_calendar = {
            "date": "2022-03-02",
            "status": 1,
            "is_english": True,
            "is_levi_signature": True,
            "is_pr": True,
            "collaborator_id": 10,
            "task_id": 11
        }
        result = requests.post(
            url=self.url_base_calendar, headers=self.headers, data=new_calendar)

        assert result.status_code == 201

    def test_put_calendar(self):
        update_calendar = {
            "date": "2023-04-02",

        }
        result = requests.put(
            url=f'{self.url_base_calendar}4/', headers=self.headers, data=update_calendar)

        assert result.status_code == 200

    def test_delete_calendar(self):
        result = requests.delete(
            url=f'{self.url_base_calendar}3/', headers=self.headers)

        assert result.status_code == 204
