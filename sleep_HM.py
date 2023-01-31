from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# init driver
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.maximize_window()
# open the url
driver.get('https://www.amazon.com/')
driver.find_element(By.ID,'glow-ingress-line2').click()
#driver.find_element(By.XPATH,"//input[@class='GLUX_Full_Width a-declarative']").send_keys('95129')
driver.find_element(By.ID,'GLUXZipUpdateInput').send_keys('95129')
driver.implicitly_wait(10)
#driver.wait =WebDriverWait(driver,10)
driver.wait.until(EC.element_to_be_clickable(By.XPATH,"//input[@class='a-button-input']"))
driver.find_element(By.XPATH,"//input[@class='a-button-input']").click()





