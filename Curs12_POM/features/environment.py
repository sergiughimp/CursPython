from browser import Browser
from pages.login_page import LoginPage
from pages.inventory import InventoryPage

def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser)
    context.inventory_page = InventoryPage(context.browser)

def after_scenario(context, scenario):
    context.browser.quit()
