import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# EDIT CODE HERE:
login_page_url = ""
college_enroll = ""
password = ""

browser = webdriver.Chrome()
try:
    browser.get(login_page_url)
    username_element = browser.find_element(By.ID, "username")
    username_element.send_keys(college_enroll)
    password_element = browser.find_element(By.ID, "password")
    password_element.send_keys(password)
    signInButton = browser.find_element(By.ID, "loginbutton")
    signInButton.click()
    time.sleep(2)
    browser.quit()
except:
    print("ERROR OCCURRED!")
