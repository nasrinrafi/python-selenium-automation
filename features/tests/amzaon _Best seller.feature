# Created by ross at 1/6/23
Feature: test for verify for links
  Scenario: user can click links from bestseller

    Given :open amazon bestseller link
    When :click Bestseller
    Then :verify able to open <result>

    Given :open amazon bestseller link
    When :click mover ad shaker link
    Then :verify able to open <result>

    Given :open amazon bestseller link
    When :click Most wished for
    Then :veri able to open <result>


    Example:
      |links        | result
      |Bestseller     | "Bestseller link"
      |Mover and shaker |"mover and shaker"
      |Most wished for   |"most wished for"
      |Gift idea         |"gift idea"



