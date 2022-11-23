'''
Implementează o clasă Login care să moștenească unittest.TestCase
Gasește elementele în partea de sus folosind ce selectors dorești:
- setUp()
- Driver
https://the-internet.herokuapp.com/
Click pe Form Authentication
tearDown()
Quit browser
'''

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        service = ChromeService(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(10)
        self.driver.get("https://the-internet.herokuapp.com/")
        self.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.quit()

    # ● Test 1
    # - Verifică dacă noul url e corect

    def test1_url_corect(self):
        form_authentication = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        form_authentication.click()
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(self.driver.current_url, expected_url, "URL-ul nu este cel asteptat!")

    # ● Test 2
    # - Verifică dacă page title e corect

    # def test2_page_title_corect(self):
    #     page_title = self.driver.find_element(By.XPATH, "//title")
    #     print(page_title.text)
    #     assert page_title.text == "The Internet", "Titlu-ul paginei nu este cel asteptat!"
    #     self.assertEqual(page_title.text, "The Internet", "Titlu-ul paginei nu este cel asteptat!")

    # ● Test 3
    # - Verifică textul de pe elementul xpath=//h2 e corect

    def test3_h2_corect(self):
        element_h2 = self.driver.find_element(By.TAG_NAME, "h2")
        assert element_h2.text == "Available Examples"

    # ● Test 4
    # - Verifică dacă butonul de login este displayed

    # def test4_login_button_is_displayed(self):
    #     login_button = self.driver.find_element()

    # ● Test 5
    # - Verifică dacă atributul href al linkului ‘Elemental Selenium’ e corect

    def test5_href_link(self):
        form_authentication = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        form_authentication.click()
        href_link = self.driver.find_element(By.XPATH, '//a[@target="_blank"]')
        assert href_link.text == "Elemental Selenium"

    # ● Test 6
    # - Lasă goale user și pass
    # - Click login
    # - Verifică dacă eroarea e displayed

    def test6_login(self):
        expected_text = 'Your username is invalid!'
        form_authentication = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        form_authentication.click()
        login_button = self.driver.find_element(By.CLASS_NAME, 'fa-sign-in')
        login_button.click()
        alert_text = self.driver.find_element(By.ID, 'flash')
        # assert alert_text.text == expected_text, "Text doesn't match"
        print(alert_text.text)

    # ● Test 10
    # - Completează cu user și pass valide
    # - Click login
    # - Verifică ca noul url CONTINE /secure

    def test_10(self):
        form_authentication = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        form_authentication.click()
        user_form = self.driver.find_element(By.ID, 'username')
        user_form.send_keys("tomsmith")
        time.sleep(3)
        password_form = self.driver.find_element(By.ID, 'password')
        password_form.send_keys("SuperSecretPassword!")
        time.sleep(3)
        login_button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        login_button.click()
        time.sleep(3)
        assert '/secure' in self.driver.current_url


    # ● Test 11
    # - Completează cu user și pass valide
    # - Click login
    # - Click logout
    # - Verifică dacă ai ajuns pe https://the-internet.herokuapp.com/login

    def test_11_login_logout(self):
        form_authentication = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        form_authentication.click()
        user_form = self.driver.find_element(By.ID, 'username')
        user_form.send_keys("tomsmith")
        time.sleep(3)
        password_form = self.driver.find_element(By.ID, 'password')
        password_form.send_keys("SuperSecretPassword!")
        time.sleep(3)
        login_button = self.driver.find_element(By.CLASS_NAME, 'fa-sign-in')
        login_button.click()
        time.sleep(3)
        logout_button = self.driver.find_element(By.CSS_SELECTOR, 'a.button.secondary.radius')
        logout_button.click()