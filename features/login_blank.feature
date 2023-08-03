Feature: Validate the login feature

Scenario: Login without entering any credentials
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in website
    Then The login portal has been opened
    When Provide the email "" and password ""
    Then Please enter a valid email address and This field cannot be blank message is displayed
    Then Click on the Sign in button
    Then Login is failed and invalid email or password message is displayed
    Then Close the browser