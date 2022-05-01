import requests


# Testing task
class Test_tasks:
    headers = {'Authorization': 'Token 1dd9d4875c392a6389b78379e71dd0e21cf799a4'}
    url_base_task = 'http://0.0.0.0:8000/api/v1/task/'

    def test_get_all_tasks(self):
        tasks = requests.get(
            url=self.url_base_task, headers=self.headers)

        assert tasks.status_code == 200

    def test_get_task(self):
        task = requests.get(
            url=f'{self.url_base_task}7/', headers=self.headers)

        assert task.status_code == 200

    def test_post_task(self):
        new_task = {
            "title": "string",
            "description": "string",
            "date_in_todo": "2022-09-02",
            "date_in_progress": "2022-07-02",
            "date_in_review": "2022-04-02",
            "date_done": "2022-02-02",
            "date_blocked": "2022-01-02",
            "date_expected": "2022-06-02",
            "estimate": 5,
            "link_branch": "string",
            "pr_link": "string",
            "total_commits": 10,
            "link_video": "string",
            "status_task_id": 16,
            "project_id": 15
        }
        result = requests.post(
            url=self.url_base_task, headers=self.headers, data=new_task)

        assert result.status_code == 201

    def test_put_task(self):
        update_task = {
            "title": "Project test",
            "description": "Pytest",
            "date_in_todo": "2022-03-03",
            "date_in_progress": "2022-03-04",
            "date_in_review": "2022-03-05",
            "date_done": "2022-03-06",
            "date_blocked": "2022-03-07",
            "date_expected": "2022-03-08",
            "estimate": 4,
            "link_branch": "http://0.0.0.0:8000/api/v1/task/",
            "pr_link": "http://0.0.0.0:8000/api/v1/task/",
            "total_commits": 6,
            "link_video": "http://0.0.0.0:8000/api/v1/task/",
            "status_task_id": 3,
            "project_id": 5
        }
        result = requests.put(
            url=f'{self.url_base_task}4/', headers=self.headers, data=update_task)

        assert result.status_code == 200

    def test_delete_task(self):
        result = requests.delete(
            url=f'{self.url_base_task}3/', headers=self.headers)

        assert result.status_code == 204
