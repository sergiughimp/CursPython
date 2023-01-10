from selenium.webdriver.common.by import By


class InventoryPage():

    URL = 'https://www.saucedemo.com/inventory.html'
    TITLE_SELECTOR = (By.CLASS_NAME, 'title')
    PRODUCTS_SELECTOR = (By.CLASS_NAME, 'inventory_item')

    def __init__(self, browser):
        self.driver = browser.driver

    def get_page(self):
        self.driver.get(self.URL)

    def get_page_title(self):
        title_element = self.driver.find_element(*self.TITLE_SELECTOR)
        return title_element.text

    def get_products_count(self):
        products = self.driver.find_elements(*self.PRODUCTS_SELECTOR)
        return len(products)