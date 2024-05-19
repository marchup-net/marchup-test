# Run this script using locust. You can control locust by accessing http://127.0.0.1:8089
# Use pip install to download required python files including locust
# In order to automatically restart locust when the script is updated you can use nodemon (installed with npm) as follows
#     nodemon --exec "locust -f MarchupGetPerf.py" --watch MarchupGetPerf.py

import os
from locust import HttpUser, task, between
from bs4 import BeautifulSoup  # You'll need BeautifulSoup installed (`pip install beautifulsoup4`)

# Ensure required environment variables are set
required_env_vars = ['MARCHUP_USERNAME', 'MARCHUP_PASSWORD']
for var in required_env_vars:
    if var not in os.environ:
        raise EnvironmentError(f"Required environment variable {var} is not set.")

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
        # Read username and password from environment variables
        username = os.getenv('MARCHUP_USERNAME')
        password = os.getenv('MARCHUP_PASSWORD')
        
        #print("Logging in user " + username + " password " + password)

        # Ensure the POST data is structured correctly, considering how your backend expects it
        login_data = {
            '_csrf': csrf_token,
            'Login[username]': username,
            'Login[password]': password,
            'Login[rememberMe]': '1'
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': self.client.base_url + "/user/auth/login"
        }

        with self.client.post("/user/auth/login", data=login_data, headers=headers, allow_redirects=False, catch_response=True) as response:
            if response.status_code in [200, 302] and '_identity' in response.cookies:
                response.success()
            else:
                print("Login failed. Identity cookie not found or incorrect status code " + str(response.status_code))
                response.failure("Failed to log in. Identity cookie not set.")

    @task
    def after_login(self):
        """A task that runs after login. Example: Load the dashboard page."""
        #print("Fetch dashboard and spaces")
        self.client.get("/dashboard")
        self.client.get("/spaces")

