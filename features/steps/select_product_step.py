from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium import webdriver

@given( 'open amazon product{product_id} page')
def open_page(context,product_id):
     context.driver.get('https://www.amazon.com/gp/product/product_id/')
@then('able to select product through color')
def select_product(context):
     expected_color=['Black','Blue, Over Dye','Light Wash',
                     'Bright White','Dark Blue Vintage',
                     'Dark Indigo/Rinsed','Dark Khaki Brown',]
     actual_color=[]
     colors = context.driver.find_element(By.CSS_SELECTOR,'#variation_color_name')
     for color in colors[:9]:
          color.click()
     color_name=context.driver.find_element(By.CSS_SELECTOR,'.selection').text
     actual_color+=[color_name]
     assert actual_color==expected_color

