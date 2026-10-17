"""AttendX - Attendance Marking Test
Logs in as faculty, opens a lecture and marks a student present.
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:8080/attendx"


def login(driver):
    driver.get(BASE_URL + "/login")
    driver.find_element(By.ID, "username").send_keys("faculty01")
    driver.find_element(By.ID, "password").send_keys("Faculty@123")
    driver.find_element(By.ID, "loginBtn").click()


def test_mark_present():
    driver = webdriver.Chrome()
    login(driver)
    driver.get(BASE_URL + "/lecture/CS301")
    driver.find_element(By.ID, "student-23CS001-present").click()
    driver.find_element(By.ID, "saveAttendance").click()
    msg = driver.find_element(By.CLASS_NAME, "alert-success").text
    assert "Attendance saved" in msg
    driver.quit()


if __name__ == "__main__":
    test_mark_present()
    print("Attendance marking test passed")
