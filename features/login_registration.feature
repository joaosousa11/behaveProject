Feature: Validate the login feature

  Scenario: Registration login
    Given Launch the browser
    When Open the https://courses.ultimateqa.com/users/sign_in website
    Then The login portal has been opened
    When Do not insert any credentials
    Then Click on the Create a new account button
    Then Please insert the information for the new account and Click on Sign up button
    Then Login is successful (no message) and dashboard is opened
    Then Logout the application
    Then Close the browser
