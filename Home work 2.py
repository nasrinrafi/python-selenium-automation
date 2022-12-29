from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ross/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.get('https://www.amazon.com/')
driver.find_element(By.ID,'twotabsearchtextbox').send_keys('zippo')
driver.find_element(By.XPATH, 'span[@class="nav-cart-icon nav-sprite"]')
driver.find_element(By.XPATH ,'span[@class="a-size-base a-text-bold"]')
Input = driver.find_element(By.Id ,'input[@type="text]')
Input.send_keys('nasrin')
password = driver.find_element(By.XPATH,'lable[@for="ap_email"]')
password.send_keys('Hello')
checkbox =driver.find_element(By.XPATH,'i[@class="a-icon a-icon-checkbox]').click()
driver.find_element(By.ID,'continue').click()




