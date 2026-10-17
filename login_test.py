"""AttendX - Login Test
Checks that a registered faculty user can log in to AttendX.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8080/attendx"


def test_valid_login():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + "/login")
    driver.find_element(By.ID, "username").send_keys("faculty01")
    driver.find_element(By.ID, "password").send_keys("Faculty@123")
    driver.find_element(By.ID, "loginBtn").click()
    assert "Dashboard" in driver.title
    driver.quit()


if __name__ == "__main__":
    test_valid_login()
    print("Login test passed")


def test_invalid_password():
    driver = webdriver.Chrome()
    driver.get(BASE_URL + "/login")
    driver.find_element(By.ID, "username").send_keys("faculty01")
    driver.find_element(By.ID, "password").send_keys("wrong-pass")
    driver.find_element(By.ID, "loginBtn").click()
    error = driver.find_element(By.ID, "errorMsg").text
    assert "Invalid username or password" in error
    driver.quit()
