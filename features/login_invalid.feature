Feature: Validate the login feature

  Scenario: Login with invalid credentials
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in website
    Then The login portal has been opened
    When Provide the email "invalidemail@gmail.com" and password "testeserror"
    Then Click on the Sign in button
    Then Login is failed and invalid message is displayed
    Then Close the browser
