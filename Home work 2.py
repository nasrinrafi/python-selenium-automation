from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get('https://www.amazon.com/')
driver.find_element(By.XPATH, "//a[@href='/gp/css/order-history?ref_=nav_orders_first']")

driver.find_element(By.ID,id="ap_email").send_keys("nasrinrafi2000@gmail.com")
driver.find_element((By.ID,"continue"))
driver.find_element(By.XPATH,"//span[@class='a-expander-prompt']")




