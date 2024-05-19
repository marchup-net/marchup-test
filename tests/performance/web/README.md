# Performance Web Tests

This directory contains performance test scripts for the web components of the Marchup project.

## Files

- **MarchupGetPerf.py:** Performance testing script using Locust.

## Installation

To run the performance tests, you need to install the required dependencies.

1. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    ```

2. Install the required Python packages:
    ```bash
    pip install locust beautifulsoup4
    ```

## Environment Variables

Ensure that the following environment variables are set before running the tests:

- `MARCHUP_USERNAME`: Your Marchup username.
- `MARCHUP_PASSWORD`: Your Marchup password.

You can set these variables in your terminal session as follows:

```bash
export MARCHUP_USERNAME="your_username"
export MARCHUP_PASSWORD="your_password"
```

On Windows, use the `set` command:

```cmd
set MARCHUP_USERNAME=your_username
set MARCHUP_PASSWORD=your_password
```

## Running Tests

To run the performance tests using Locust, follow these steps:

1. Ensure your virtual environment is activated:
    ```bash
    source venv/bin/activate  # On macOS/Linux
    .\venv\Scripts\activate  # On Windows
    ```

2. Start Locust:
    ```bash
    locust -f MarchupGetPerf.py
    ```

3. Open your web browser and navigate to `http://127.0.0.1:8089` to access the Locust web interface.

4. In the Locust web interface:
    - Set the number of total users to simulate.
    - Set the spawn rate (users per second).
    - Set the host to your Marchup API URL (e.g., `https://trial.marchup.net`).
    - Click the "Start swarming" button to begin the test.

## Notes

- Ensure that the Locust file (`MarchupGetPerf.py`) is in the same directory where you run the `locust` command.
- You can control Locust by accessing the web interface at `http://127.0.0.1:8089`.
- To automatically restart Locust when the script is updated, you can use nodemon (installed with npm):
    ```bash
    nodemon --exec "locust -f MarchupGetPerf.py" --watch MarchupGetPerf.py
    ```

Feel free to update the test parameters and tasks in the `MarchupGetPerf.py` file to suit your performance testing requirements.

