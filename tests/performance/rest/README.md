# Locust Load Testing

## Installation

Install Locust using the following command:

```bash
python3 -m venv venv
source venv/bin/activate
pip install locust
```

## Configuration

Change the constants in `constant.py`:

- Set `testSpaceId` to the ID of the space you are using to test.
- Set `username` and `password` to your username and password.

## Running Locust

Start Locust by running the following command in the directory with `locustfile.py`:

```bash
locust
```

Go to the web interface.

## Configuration in Web Interface

- Change the number of users to the total number of users you want to test at max load.
- Change the ramp-up rate to the number of users added per second.
- Change the host to the API URL and start the test.
