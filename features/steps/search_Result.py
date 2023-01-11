from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given,when,then
 @then('search result for drees are shown')
      def verify_serach (context):
   assert 'dress' in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
print('Test Passed')
