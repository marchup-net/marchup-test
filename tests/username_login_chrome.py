from selenium import webdriver
from selenium.webdriver.common.by import By


def test_username_login():
    driver = webdriver.Chrome()

    driver.get("https://trial.marchup.net/")


    title = driver.title
    assert title == "Login - Marchup"
    
    driver.implicitly_wait(0.5)

    username_input = driver.find_element(by=By.ID, value="login_username")
    password_input = driver.find_element(by=By.ID, value="login_password")
    log_in = driver.find_element(by=By.ID, value="login-button")

    username_input.send_keys("testAccount")
    password_input.send_keys("password")
    log_in.click()
    driver.implicitly_wait(15)
    message = driver.find_element(by=By.ID, value="account-dropdown-link")
  
    assert message.is_displayed()

    driver.quit()