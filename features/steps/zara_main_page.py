import unittest
from selenium import webdriver

class MainPage(unittest.TestCase):

   def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.zara.com/us/')


   def test(self):
      driver = self.driver

   def search_product(self):
      search = self.driver.find_element_by_Name("search").click()
      search.send_key('pink dress')

   def size(self):
     size =self.driver.find_element(By.ID,'product-size-selector-242658679-item-0').click()

   def add_to_card(self):
     Add_to_card=self.driver.find_element(By.CssSelector,'div.zds-button__lines-wrapper').click()




   def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
