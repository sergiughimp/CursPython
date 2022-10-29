'''

1. time.sleep(x) -> Codul "doarme" x secunde
    -> indiferent daca elementul cautat, sau evenimentul pe care il asteptam apare dupa mai putin timp, Python va astepta totusi x secunde
    -> testele o sa aiba un timp mai mare de rulare, iar mare parte din acesta va fi irosit asteptand

2. selenium -> wait explicit
    -> atunci cand ii zicem lui Selenium sa astepte in mod explicit dupa o anumita conditie
    -> WebDriverWait(chrome, 10) -> cream un obiect de tipul WebDriverWait care asteapta maxim 10 secunde
    -> EC.presence_of_element_located((By.ID, logo_xpath))
        -> EC = expected condition
        -> presence_of_element_located = condition dupa care asteptam
    -> se va astepta maxim 10 secunde, dar selenium verifica la fiecare la 0.5 secunde daca elementul a aprut
3. selenium -> wait implicit
    -> se seteaza o singura data per driver, apoi de fiecare daca cand incercam sa gasim un element, actioneaza ca un wait explicit pentru gasirea acestuia

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = ChromeService(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=service)

chrome.get("http://automationpractice.com/index.php")
# Daca butonul de cart nu ar putea fi clickable, am putea folosi un explicit wait
# cart_button = chrome.find_element(By.XPATH, '//div[@class="shopping_cart"]/a')
# cart_button.click()

# Asteptam in mod explicit ca butonul cautat sa fie clickable
cart_button = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="shopping_cart"]/a')))

logo_xpath = '//img[@class="logo img-responsive"]'

# in cazul in care elementul pe care il cautam nu este inca disponibil, putem face un explicit wait
# logo_selector = chrome.find_element(By.XPATH, logo_xpath)

element = WebDriverWait(chrome, 10).until(EC.presence_of_element_located((By.ID, logo_xpath)))
print(f"Am gasit elementul:{element}")

# incepand de aici incolo, pentru orice element cautat, selenium va incerca sa-l gaseasca timp de 10 secunde (tot in intervale de 0.5 secunde)
chrome.implicitly_wait(10) # 10 secunde