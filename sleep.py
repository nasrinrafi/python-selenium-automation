from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions as EC
# init driver
driver = webdriver.Chrome(executable_path='/Users/ross/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.Id,'nav-hamburger-menu')
driver.implicitly_wait(10)
sleep(40)
driver.wait =webdriver.wait(driver,10)
driver.wait.until()





