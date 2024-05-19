from locust import HttpUser, task, between
import random, string
import constants, time

# base url: http://localhost/api/v1
# url: https://trial.marchup.net/api/v1



class HelloWorldUser(HttpUser):
    
    wait_time = between(5, 10)
    
    def on_start(self):
        adminData = {
            "username":constants.username,
            "password":constants.password
        }

        
        x = self.client.post("/auth/login", json = adminData)
        
        self.authtoken = {
            'Authorization': 'Bearer ' + x.json()['auth_token'],
            }
        self.authtoken2 = {
            'Authorization': 'Bearer ' + x.json()['auth_token'],
            'Content-Type': 'application/json'
            }
        
        self.testSpace1 = constants.testSpaceID
        
        self.testSpace1containerID = self.client.get(f"/space/{constants.testSpaceID}", headers=self.authtoken).json()['contentcontainer_id']
        
    @task(1)
    def activity(self):
        x = self.client.get("/activity", headers=self.authtoken).json()['results']
        if len(x) != 0:
            x = x[0]['id']
        x = self.client.get(f"/activity/{x}", headers = self.authtoken)
        x = self.client.get(f"/activity/container/{self.testSpace1containerID}", headers = self.authtoken)
        
        # print(x.text)
              
    @task(1)
    def notifications(self):
        x = self.client.get("/notification", headers=self.authtoken).json()['results']
        if len(x) != 0:
            x = x[0]['id']
        self.client.get(f"/notification/{x}", headers=self.authtoken)
        self.client.get("/notification/unseen", headers=self.authtoken)
        self.client.patch("/notification/mark-as-seen", headers=self.authtoken2)
        # print(x.text)
        
    @task(1)
    def spaces(self):
        x = self.client.get("/space?param=participant", headers=self.authtoken)
        
        info = self.client.get(f"/space/{self.testSpace1}", headers=self.authtoken).json()
        
        info = '''{
            "name": "Testing Space 1",
            "description": "test description",
            "visibility": 1,
            "join_policy": 1
        }'''
        
        self.client.get(f"/space/{self.testSpace1}/membership", headers=self.authtoken)
        self.client.put(f"/space/{self.testSpace1}", headers=self.authtoken2, data=info)
  
    @task(1)
    def getTopics(self):
        x = self.client.get("/topic", headers=self.authtoken)
        x = self.client.get(f"/topic/container/{self.testSpace1containerID}", headers=self.authtoken).json()['results'][0]['id']
        # x = self.client.post(f"/topic/container/{self.testSpace1containerID}", headers=self.authtoken)
        y = {
            "name": "my asdf"
        }
        self.client.put(f"/topic/{x}", headers=self.authtoken,data=y)
        x = self.client.get(f"/topic/{x}", headers=self.authtoken)
    
    @task(1)
    def wiki(self):
        self.client.get("/wiki", headers=self.authtoken)
        x = self.client.get(f"/wiki/container/{self.testSpace1containerID}", headers=self.authtoken).json()['results'][0]['id']
        y = '''{
	"WikiPage": {
		"title": "updated",
		"is_home": 0,
		"admin_only": 0,
		"is_category": 0,
		"parent_page_id": 0
	},
	"WikiPageRevision": {
		"content": "test content updated"
	},
	"PageEditForm": {
		"isPublic": 1,
		"topics": [
			17,
			13
		]
	}
}'''
        self.client.put(f"/wiki/page/{x}", headers=self.authtoken2, data=y)
        self.client.get(f"/wiki/page/{x}/revisions", headers=self.authtoken)

    @task(1)
    def mail(self):
        x = self.client.get("/mail", headers=self.authtoken)
        # print(x.text)
    
    @task(1)
    def calendar(self):
        zs = '''{
            "CalendarEntry": {
                "title": "test api calendar entry",
                "description": "test api description",
                "color": "#6fdbe8",
                "all_day": 1,
                "participation_mode": 2,
                "max_participants": "",
                "allow_decline": 1,
                "allow_maybe": 1,
                "participant_info": ""
            },
            "CalendarEntryForm": {
                "is_public": 0,
                "start_date": "2025-03-19",
                "start_time": "10:00",
                "end_date": "2025-03-31",
                "end_time": "19:30",
                "timeZone": "Europe/Helsinki",
                "forceJoin": 1,
                "topics": ""
            }
        }'''
        
        self.client.get("/calendar", headers=self.authtoken)
        
        self.client.get(f"/calendar/container/{self.testSpace1containerID}", headers=self.authtoken)

        x = self.client.post(f"/calendar/container/{self.testSpace1containerID}", headers=self.authtoken2, data = zs).json()['id']
        
        self.client.get(f"/calendar/entry/{x}", headers=self.authtoken, name="/calendar/entry/[id]")
        
        self.client.put(f"/calendar/entry/{x}", headers=self.authtoken2, data=zs, name="/calendar/entry/[id]")
        self.client.delete(f"/calendar/entry/{x}", headers=self.authtoken, name="/calendar/entry/[id]")
        # print(x.text)

    @task(1)
    def taskss(self):
        self.client.get(f"/tasks/container/{self.testSpace1containerID}", headers=self.authtoken)
        
        y = '''{
            "Task": {
                "title": "First api task",
                "description": "First api task for test space 2",
                "task_list_id": null,
                "scheduling": 1,
                "all_day": 0,
                "selectedReminders": [
                    1,
                    2,
                    8
                ],
                "cal_mode": 1,
                "assignedUsers": [
                    "ad82fbfa-9621-489f-993a-0cf6d8be5747"	
                ],
                "responsibleUsers": [
                    "ad82fbfa-9621-489f-993a-0cf6d8be5747"	
                ],
                "review": 1
            },
            "TaskForm": {
                "is_public": 1,
                "start_date": "2019-03-29",
                "start_time": "10:00",
                "end_date": "2019-03-31",
                "end_time": "19:30",
                "timeZone": "Europe/Helsinki",
                "newItems": [
                    "first",
                    "second",
                    "third"
                ]
            }
        }'''
        x = self.client.post(f"/tasks/container/{self.testSpace1containerID}", headers=self.authtoken2, data=y).json()['id']
        time.sleep(0.001)
        
        self.client.put(f"/tasks/task/{x}", headers=self.authtoken2, data=y, name="/tasks/task/[id]")
        time.sleep(0.001)
        self.client.delete(f"/tasks/task/{x}", headers=self.authtoken, name="/tasks/task/[id]")
        