Feature: Validate the login feature

  Scenario: Login with valid credentials
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in website
    Then The login portal has been opened
    When Provide the email "jfilipesousa1991@gmail.com" and password "testesmartex"
    Then Click on the Sign in button
    Then Login is successful and dashboard is opened
    Then Logout the application
    Then Close the browser
