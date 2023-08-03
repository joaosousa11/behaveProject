from behave import *
from features.config import Config
from features.pages.LoginPage import LoginPage
from features.pages.HomePage import HomePage


# Valid Login Steps


@when(u'Provide the email "jfilipesousa1991@gmail.com" and password "testesmartex"')
def set_valid_credentials(context):
    global login
    login = LoginPage(context.driver, Config.VALID_USER, Config.VALID_PASSWORD)


@then(u'Click on the Sign in button')
def click_sign_in(context):
    LoginPage.click_sign_in_btn(login)


@then(u'Login is successful and dashboard is opened')
def is_login_successfully(context):
    global home
    home = HomePage(context.driver)


@then(u'Logout the application')
def click_logout(context):
    HomePage.click_logout(home)


# Invalid Login Steps


@when(u'Provide the email "invalidemail@gmail.com" and password "testeserror"')
def set_invalid_credentials(context):
    global login
    login = LoginPage(context.driver, Config.INVALID_USER, Config.INVALID_PASSWORD)


@then(u'Login is failed and invalid message is displayed')
def is_invalid_login(context):
    LoginPage.is_invalid_user(login)


# Blank Login Steps

@when(u'Provide the email "" and password ""')
def set_blank_credentials(context):
    global login
    login = LoginPage(context.driver)


@then(u'Please enter a valid email address and This field cannot be blank message is displayed')
def is_invalid_login(context):
    LoginPage.set_blank_fields(login)


@then(u'Login is failed and invalid email or password message is displayed')
def is_blank_login(context):
    LoginPage.is_invalid_user(login)


# Registration Login Steps

@when(u'Do not insert any credentials')
def pass_credentials(context):
    global login
    login = LoginPage(context.driver)


@then(u'Click on the Create a new account button')
def click_create_account(context):
    LoginPage.click_create_account(login)


@then(u'Please insert the information for the new account and Click on Sign up button')
def set_info_sign_up(context):
    LoginPage.create_new_account(login, Config.FNAME, Config.LNAME,
                                 Config.EMAIL, Config.PASSWORD)


@then(u'Login is successful (no message) and dashboard is opened')
def is_login_no_message(context):
    global home
    home = HomePage(context.driver, True)

