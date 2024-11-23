from locust import HttpUser, task, between

class LoadTest(HttpUser):
    wait_time = between(1, 3)  # Ожидание между запросами от 1 до 3 секунд

    @task
    def send_email(self):
        self.client.post("/tasks/send_email/", {
            'recipient': 'test@example.com',
            'subject': 'Test Subject',
            'body': 'Test Body'
        })

    @task
    def view_homepage(self):
        self.client.get("/")
