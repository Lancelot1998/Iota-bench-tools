
from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def profile(self):
        self.client.get("/transaction")
   
    @task
    def profile_two(self):
    	self.client.get("/node")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 1000
