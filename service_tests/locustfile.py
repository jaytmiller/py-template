from locust import HttpUser, task


class CheckAlive(HttpUser):
    @task
    def check_alive(self):
        self.client.get("/check-alive")
