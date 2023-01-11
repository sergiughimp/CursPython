Feature: Inventory Page

#  @single
  Scenario: Has 6 products on page
    Given I am on the Sign in page
    When I login successfully with "standard_user" and "secret_sauce"
    Then There are 6 products on the Inventory page

  Scenario: Redirect to Login page when unauthenticated user
    Given I am not a log in user
    When I go to the Inventory Page
    Then I am redirected to Login Page
    And I receive a Sad Face message

  @single
  Scenario: Add object to cart
    Given I am a logged in user
    And I am on the Inventory Page
    When I add a product to cart
    Then The 'Add to cart' button changes to 'remove' button
    And The cart counter is incremented by one