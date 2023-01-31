from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()
driver.get('https://shop.mango.com/us')
driver.find_element(By.XPATH,"//span[text()='Women']").click()
driver.find_element(By.xpath,"//input[@class='SdgBo'])").send_keys('coat')

#driver.find_element(By.ID,"onetrust-accept-btn-handler").click()
#driver.find_element(By.ID,'searchIconButton').send_keys('pants')
#driver.find_element(By.ID,"//div[text()='brown trousers']").click()



