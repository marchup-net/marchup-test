import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from time import sleep 
#tabbing and entering is a temporary solution for these tests, must be fixed later with a better way to identify elements
driver_pick = input("Chrome, Firefox, or Safari?")
if driver_pick.lower() == "chrome":
    driver = webdriver.Chrome()
elif driver_pick.lower() == "safari":
    driver = webdriver.Safari()
elif driver_pick.lower() == "firefox":
    driver = webdriver.Firefox()
else:
    raise ValueError("Incorrect input. Please correctly spell one of the three browsers.")
wait = WebDriverWait(driver, 10)
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.common.keys

actions = ActionChains(driver)
@pytest.fixture(scope="session")
def logged_in():
    driver.get("https://trial.marchup.net/")


    title = driver.title
    assert title == "Login - Marchup"

    driver.implicitly_wait(0.5)

    username_input = wait.until(EC.presence_of_element_located((By.ID, "login_username")))
    password_input = wait.until(EC.presence_of_element_located((By.ID, "login_password")))
    log_in = wait.until(EC.element_to_be_clickable((By.ID, "login-button")))

    username_input.send_keys("testAccount")
    password_input.send_keys("password")
    log_in.click()
    message = wait.until(EC.presence_of_element_located((By.ID, "account-dropdown-link")))
    assert message.is_displayed()
def test_username_login(logged_in):
    pass
def test_create_space(logged_in):
    spaceButton = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Spaces")))
    assert spaceButton.is_displayed()
    spaceButton.click()
    message = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create a New Space")))
    assert message.is_displayed()
    message.click()
    sleep
    spaceName=wait.until(EC.presence_of_element_located((By.ID, "space-name")))
    spaceName.send_keys("Space Name Temporary")
    sleep(1)
    spaceDescription=wait.until(EC.presence_of_element_located((By.ID, "space-description")))
    spaceDescription.send_keys("Space Description Temporary")
    sleep(1)
    spaceLocation=wait.until(EC.presence_of_element_located((By.ID, "space-location")))
    spaceLocation.send_keys("San Jose, CA")
    sleep(1)
    for i in range(4):
        actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()

    sleep(1.5)
    for i in range(7):
        actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    sleep(1.5)
    for i in range(2):
        actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    sleep(3.5)
    driver.get("https://trial.marchup.net/s/space-name-temporary/space/manage/default/delete")
    spaceDelete=wait.until(EC.presence_of_element_located((By.ID, "deleteform-confirmspacename")))
    spaceDelete.send_keys("Space Name Temporary")
    sleep(3.3)
    actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    sleep(3.5)
    for i in range(3):
        actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    sleep(4)
def test_message(logged_in):

    driver.get("https://trial.marchup.net/mail/mail/index")
    create = wait.until(EC.presence_of_element_located((By.ID, "mail-conversation-create-button")))
    create.click()
    sleep(0.3)
    actions.send_keys("kundan").perform()
    sleep(0.5)
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    sleep(0.3)
    actions.send_keys("Test Message").perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys("Last Test1").perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys(selenium.webdriver.common.keys.Keys.ENTER).perform()
    pass
def test_search_Jobs(logged_in):
    driver.get("https://trial.marchup.net/jobs/global")
    for i in range(11):
        actions.send_keys(selenium.webdriver.common.keys.Keys.TAB).perform()
    actions.send_keys("Job Test").perform()
    sleep(5)
    job3 = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(@class, 'media-heading') and contains(., 'Job Test #3')]")))
    assert job3.is_displayed
    job3.click()
    sleep(3)
    driver.back()
    job2 = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(@class, 'media-heading') and contains(., 'Job Test #2')]")))
    assert job2.is_displayed
    job2.click()
    sleep(3)
    driver.back()
    job1 = wait.until(EC.presence_of_element_located((By.XPATH, "//h4[contains(@class, 'media-heading') and contains(., 'Job Test #1')]")))
    assert job1.is_displayed
    job1.click()
    sleep(3)