from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.firefox.options import Options as firefoxOption
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import service
from selenium.webdriver.firefox.options import Options

driver = webdriver.Firefox(executable_path="./geckodriver")
def browser_init(context):
 context.driver = webdriver.Firefox(executable_path="./geckodriver")
Options = firefoxOption()
Options.add_argument("--Headless")
driver=webdriver.firefox(options=Options,browser=driver)




