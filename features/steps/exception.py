from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@then('sing in is click able')
def open_sing_in(context):
    # context.driver.find_element(By.ID,'nav-link-accountList').click()
    # context.driver.wait.until()
    context.driver.wait.until(EC.element_to_be_clickable((By.ID,'nav-link-accountList'))).click()
