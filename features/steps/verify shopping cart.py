from selenium.webdriver.common.by import By
from behave import given, when, then
@then('verify amazon cart has{expected_cart}')
def verify shopping_cart(context,expected_cart):
    expected_cart = 'cart is empty'
    actual_cart = context.driver.find_element(By.ID 'nav-cart-count')
    assert actual_cart=expected_cart, f'expected{expected_cart}but got {actual_cart}'
    assert context.driver.find_element(By.ID, )