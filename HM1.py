from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/Users/ross/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.get('https://www.amazon.com/')