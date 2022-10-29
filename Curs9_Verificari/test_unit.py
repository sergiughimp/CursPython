'''
Libraria unittest - importam
    -> facem o clasa de teste, care mosteneste TestCase
    -> implementam metodele necesare:
        -> setUp - ce se intampla inainte de fiecare test
        -> tearDown - ce se intampla dupa fiecare test
    -> scriem oricate metode de test dorim noi (important: numele acestora trebuie sa inceapa cu test)
'''
import unittest
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_nothing(self):
        assert 1 + 1 == 2

    def not_a_test(self):
        print("This is not a test!")

    def test_something(self):
        assert len("Sergiu") == 6

class RulesTestCase(unittest.TestCase):

    def setUp(self) -> None:

        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://jules.app/sign-in")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_forgot_password_redirect(self):
        forgot_pass_link = self.chrome.find_element(By.XPATH, '//a[@data-test-id="forgot-password-link"]')
        forgot_pass_link.click()
        expected_url = 'https://jules.app/forgot-password'
        # assert self.chrome.current_url == expected_url
        self.assertEqual(self.chrome.current_url, expected_url, "URL-ul nu este cel asteptat!")
        self.assertIn("forgot-password", self.chrome.current_url)

class EmagTestCase(unittest.TestCase):
    login_button_selector = (By.XPATH, '//a[text()="Intra in cont"]')
    card_selector = (By.XPATH, '//a[text()=" Vezi detalii cos"]')

    def setUp(self) -> None:

        service = ChromeService(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=service)
        self.chrome.implicitly_wait(10)
        self.chrome.get("https://www.emag.ro/")

    def tearDown(self) -> None:
        self.chrome.quit()

    def test_login(self):
        time.sleep(3)
        login_button = self.chrome.find_element(*self.login_button_selector)
        login_button.click()
        time.sleep(3)
    
    def test_cart(self):
        my_cart_button = self.chrome.find_element(By.ID, "my_cart")
        # my_cart_button.click()
        ActionChains(self.chrome).move_to_element(my_cart_button).perform()

        cart_details_button = self.chrome.find_element(*self.card_selector)
        cart_details_button.click()

        cart_page_title = self.chrome.find_element(By.XPATH, '//div[@class="title"]')
        self.assertEqual(cart_page_title.text, "Cosul tau este gol")