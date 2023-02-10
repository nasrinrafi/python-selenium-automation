from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='/Users/ross/Desktop/python-selenium-automation/chromedriver')
driver.maximize_window()
driver.get('https://www.amazon.com')
driver.find_element(By.ID,'nav-signin-tooltip').click()
Input=driver.find_element(By.ID,'ap_email')
Input.send_keys('nasrinrafi@gmail.com')
driver.find_element(By.ID,'continue').click()
driver.find_element(By.ID,'ap_change_login_claim').click()
driver.find_element(By.XPATH,'span[@class="a-expander-prompt"]').click()
driver.find_element((By.ID,'ap-other-signin-issues-link')).click()

#expected_test ='signin'
#actual_test =driver.find_element(By.XPATH,'').text
#assert actual_test=expected_test,f'expected{expected_test}but got {actual_test}'
#assert driver.find_element(By.ID,)