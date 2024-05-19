# Functional Web Tests

This directory contains functional test scripts for the web components of the Marchup project.

## Files

- **conftest.py:** Common configuration for pytest.
- **test_example.py:** Example test file.
- **marchup_test_framework.py:** Test framework utilities.

## Installation

Python test scripts are checked into this directory. Use `pytest` to run tests.

Tests use `pytest`, `pytest-selenium`, and `selenium`. To install them, run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install pytest pytest-selenium selenium
```

## Running Tests

To run all tests, use the command:

```bash
source venv/bin/activate
pytest marchup_test_framework.py -s
```

To run a specific test, use the command:

```bash
source venv/bin/activate
pytest marchup_test_framework.py -k FUNCTION_NAME -s
```

where `FUNCTION_NAME` is one of the functions in the `marchup_test_framework.py`.

**Note:** Use only the Chrome webdriver when prompted.
