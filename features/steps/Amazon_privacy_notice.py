from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given,when,then
@given('Open Amazon T&C page')
def open_web(contex):
    contex.driver = webdriver.Chrome(executable_path='./chromedriver')
    contex.driver.maximize_window()
    contex.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=202140280')
@when('Store original windows')
def store_orginal_window(contex):
    contex.driver=contex.driver.current_window_handel
@when('Click on Amazon Privacy Notice link (*see image below')
def click_privacy_link(contex):
    contex.driver.find_element(By.XPATH ,'//a[@href="https://www.amazon.com/privacy"]')




