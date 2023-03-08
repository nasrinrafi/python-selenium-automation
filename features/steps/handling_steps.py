from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then


@given('Open Amazon T&C page')
def open_t(context):
    context.driver.get('https://www.amazon.com/')


@when('Store original windows')
def store_current_window(context):
    context.current_window = context.driver.current_window_handle
    print(context.current_window)


@given('Click on Amazon Privacy Notice')
def click_privacy_notice(context):
    context.driver.find_element(By.CSS_SELECTOR,'a._blank').click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened())
    windows=context.driver.window_handles
    context.driver.switch_to.window(windows[1])


@then ('Verify Amazon Privacy Notice page is opened')
def page_is_open(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/privacy'))


@then('User can close new window and switch back to original')
def close_new_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.current_window)






