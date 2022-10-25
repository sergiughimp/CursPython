# https://the-internet.herokuapp.com/

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("https://the-internet.herokuapp.com/")
chrome.maximize_window()
time.sleep(2)

# css - link text selector
dynamic_controls = chrome.find_element(By.LINK_TEXT, "Dynamic Controls")
dynamic_controls.click()
time.sleep(2)

# css - selector
check_box = chrome.find_element(By.CSS_SELECTOR, "input[type='checkbox']")
check_box.click()
time.sleep(2)

# css - selector
remove_button = chrome.find_element(By.CSS_SELECTOR, "button[onclick='swapCheckbox()']")
remove_button.click()
time.sleep(5)

# id - selector
message = chrome.find_element(By.ID, "message")
assert message.text == "It's gone!", "Something is wrong!"
time.sleep(5)

chrome.close()
