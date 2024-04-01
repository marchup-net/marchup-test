from locust import HttpUser, task, between
from bs4 import BeautifulSoup  # You'll need BeautifulSoup installed (`pip install beautifulsoup4`)

class MarchupUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """Perform login when a simulated user starts."""
        response = self.client.get("/user/auth/login")
        soup = BeautifulSoup(response.text, "html.parser")
        csrf_token = soup.find('input', {'name': '_csrf'}).get('value')  # Adjust this selector based on actual HTML structure
        #print("csrf token extracted " + csrf_token)
        self.login(csrf_token)

    def login(self, csrf_token):
        # Ensure the POST data is structured correctly, considering how your backend expects it
        login_data = {
            '_csrf': csrf_token,
            'Login[username]': 'test1',  
            'Login[password]': 'test1',  
            'Login[rememberMe]': '1'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'http://127.0.0.1:8888/user/auth/login'
        }

        with self.client.post("/user/auth/login", data=login_data, headers=headers, catch_response=True) as response:
            if response.status_code in [200, 302]:
                response.success()
            else:
                response.failure(f"Failed to log in. Status code: {response.status_code}")

    @task
    def after_login(self):
        """A task that runs after login. Example: Load the dashboard page."""
        #print("Fetch dashboard and spaces")
        self.client.get("/dashboard")
        self.client.get("/spaces")
