# https://formy-project.herokuapp.com/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://formy-project.herokuapp.com/")
chrome.maximize_window()
time.sleep(2)


# class - selector
title = chrome.find_element(By.CLASS_NAME, "display-3")
assert title.text == "Welcome to Formy", "Title not found"
time.sleep(2)

# css - selector
switch_window = chrome.find_element(By.CSS_SELECTOR, "li:nth-child(17) > a")
switch_window.click()
time.sleep(2)

# id - selector
alert_button = chrome.find_element(By.ID, "alert-button")
alert_button.click()
time.sleep(2)

chrome.close()