from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='/Users/ross/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')
driver.find_element(By.ID,'twotabsearchtextbox').clear().send_key('dress')
driver.find_element(By.ID,'nav-search-submit-button').click()
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()



