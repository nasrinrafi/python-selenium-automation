# Created by ross at 3/14/23

  Scenario: verify search & add to card
    Given open zara page
    When click on search btn
    And search pink pants
    And Add to card
    Then verify add to card