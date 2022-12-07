from browser import Browser


def before_all(context):
    context.browser = Browser()


def after_all(context):
    context.browser.quit()

def after_scenario(context, scenario):
    if scenario.name == 'Successful sign in with expired membership':
        context.browser.close()