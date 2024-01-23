import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()  # Replace with your preferred browser
    yield driver
    driver.quit()
