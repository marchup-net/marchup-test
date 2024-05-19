# Tests

This directory contains all test scripts and related files for the Marchup project.

## Directory Structure

- **functional:** Contains functional tests for web components.
  - **web:**
    - **conftest.py:** Common configuration for pytest.
    - **README.md:** Documentation for functional web tests.
    - **test_example.py:** Example test file.
    - **marchup_test_framework.py:** Test framework utilities.
- **performance:** Contains performance tests for both REST APIs and web components.
  - **rest:**
    - **constants.py:** Contains constants used in the performance tests.
    - **locustfile.py:** Locust test script for performance testing.
    - **readme.txt:** Documentation for REST API performance tests.
  - **web:**
    - **src:**
      - **MarchupGetPerf.py:** Performance test script for web components.

Refer to the respective subdirectories for more details on how to run the tests.

