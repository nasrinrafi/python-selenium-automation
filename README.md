rom selenium.webdriver.common.by import By
from behave import *
from selenium import webdriver
from time import sleep

@given('Open amazon page')
def open_amzon_page (context):
  #context.driver = webdriver.Chrome(executable_path='./chromedriver')
  context.driver.get('https://www.Amazon.com/')
  context.driver.maximize_window()
  context.driver.implicitly_wait(4)

@when('Creat amazon account')
def creat_account(context):
    context.driver.find_element(By.CSS_SELECTOR,"a.nav-a nav-a-2  nav-progressive-attribute").click
    context.driver.find_element(By.CSS_SELECTOR,"span.nav-action-inner").click
    context.driver.find_element(By.CSS_SELECTOR,"i.a-icon a-accordion-radio a-icon-radio-inactive").click

@then('put your name')
def enter_name(context):
    context.driver.find_element(By.CSS_SELECTOR,"ap_customer_name").send_key('nasrin')
    assert 'nasrin' in context.driver.current_url.lower(), f"Expected query not in {context.driver.current_url.lower()}"
print('Test Passed')

@then('put phone number')
def enter_phone(context):
    context.driver.find_element(By.CSS_SELECTOR,'ap_email').send_key('40867897')

@then('put password')
def enter_password(context):
    context.driver.find_element(By.CSS_SELECTOR,"put password").send_key('khjgj')
@then('Renter password')
def enter_password2(context):
    context.driver.find_element(By.CSS_SELECTOR,"#auth-passwordCheck-missing-alert").send_key()


@then('verify creat account')
def very_create_acount(context):
    context.driver.find_element(By.ID,'continue').click()
   # expected_result="verify creat account"
   # actual_resut=  context.driver.find_element(By.ID,'continue').click()
   # assert expected_result==actual_resut


