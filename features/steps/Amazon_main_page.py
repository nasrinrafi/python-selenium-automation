from multiprocessing import context

from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given,when,then

@given('open search page')
def search_Amazon(context):
 context.driver.get('https://www.google.com/')

@when ( 'search for {product}')
def search_product(context,product):
    context.driver.find_element(By.ID,'twotabsearchtextbox').clear().send_key('product')
    context.driver.find_element(By.ID,'nav-search-submit-button').click()
