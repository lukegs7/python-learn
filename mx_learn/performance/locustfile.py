from locust import HttpUser, task, TaskSet

"""
    locust -f locustfile.py [-H http://localhost:8080]
    (1)Number of total users to simulate: 设置模拟的用户总数
    (2)Hatch rate (users spawned/second): 每秒启动的虚拟用户数
"""


class UserTask(TaskSet):
    @task(1)
    def index(self):
        self.client.get('/name')


# 用户类
class WebsiteUser(HttpUser):
    tasks = Discuz_login.tasks
    # 相邻两个请求的时间间隔-随机
    min_wait = 3000
    max_wait = 6000
    host = 'http://localhost:8000'
