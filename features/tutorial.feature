#noinspection CucumberUndefinedStep
Feature: Added a new function of "Tb Coupon Query"
  Background: user is installed the latest SAK app

  Scenario: user to get the Tb Coupon successfully
    Given user is on the home page of SAK app
    When  user click the button of "Tb Coupon Query"
    Then  user able to see the page of "精选优品"
    When  user click any one product
    Then  user able to see the page of "粉丝福利购"
    When  user click the button of "立即领券"
    Then  user able to see the page of product details on Taobao app
