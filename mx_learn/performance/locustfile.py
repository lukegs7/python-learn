from locust import HttpUser, task, between

"""
    locust -f my_locustfile.py -H http://localhost:8080
"""

class QuickstartUser(HttpUser):
    wait_time = between(5, 9)

    @task(1)
    def on_start(self):
        self.client.get("/name")

