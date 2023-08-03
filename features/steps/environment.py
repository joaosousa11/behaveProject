from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from features.config import Config


@given(u'Launch the browser')
def launch_chrome(context):
    serv = Service(executable_path=Config.CHROME_EXECUTABLE_PATH)
    opts = webdriver.ChromeOptions()
    # opts.add_argument("--headless")
    opts.add_argument("disable-infobars")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-popup-blocking")
    opts.add_argument('--profile-directory=Default')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--no-sandbox')
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument('--log-level=3')
    context.driver = webdriver.Chrome(service=serv, options=opts)


@when(u'Open the https://courses.ultimateqa.com/users/sign_in website')
def open_website(context):
    context.driver.maximize_window()
    context.driver.set_page_load_timeout(30)
    context.driver.get(Config.BASE_URL)


@then(u'The login portal has been opened')
def verify_title(context):
    get_title = context.driver.title
    get_url = context.driver.current_url
    assert get_title == Config.PAGE_NAME
    assert get_url == Config.BASE_URL


@then(u'Close the browser')
def close_browser(context):
    if context.driver is not None:
        print("EXIT: Cleanup of test environment")
        context.driver.quit()

