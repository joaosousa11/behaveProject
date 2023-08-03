Feature: Login scenarios

  Background: common steps
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in website
    Then The login portal has been opened

  Scenario: Login with valid credentials
    When Provide the email "jfilipesousa1991@gmail.com" and password "testesmartex"
    Then Click on the Sign in button
    Then Login is successful and dashboard is opened
    Then Logout the application
    Then Close the browser

  Scenario: Login with invalid credentials
    When Provide the email "invalidemail@gmail.com" and password "testeserror"
    Then Click on the Sign in button
    Then Login is failed and invalid message is displayed
    Then Close the browser

  Scenario: Login without entering any credentials
    When Provide the email "" and password ""
    Then Please enter a valid email address and This field cannot be blank message is displayed
    Then Click on the Sign in button
    Then Login is failed and invalid email or password message is displayed
    Then Close the browser

  Scenario: Registration login
    When Do not insert any credentials
    Then Click on the Create a new account button
    Then Please insert the information for the new account and Click on Sign up button
    Then Login is successful (no message) and dashboard is opened
    Then Logout the application
    Then Close the browser