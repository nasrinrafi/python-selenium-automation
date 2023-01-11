from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open amazon bestseller link')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    @when('click Bestseller')
    def click_bestseller(context):
        context.driver.find.element(By.ID,'a-popover-root').click
    @then ('verify able to open <result>')
    def verify_expected_result(context,link):
        expected_result='Bestseller'
        assert link in context.driver.find.element(By.ID,'zg_banner_text'),f"Expected query not in{expected_result}but got{context.driver.find.element(By.ID,'zg_banner_text')}"
    @when ('click mover ad shaker link')
    def click_mover_shaker(context):
        context.driver.find.element(By.XPATH,'div[@class_p13n-zg-nav-tab-all_style_zg-mobile-tabs-li-div__11Bpr]').click

    @then('verify able to open <result>')
    def verify_expected_result(context, link):
      expected_result = 'shaker link'
      assert link in context.driver.find.element(By.ID,'zg_banner_text),'f"Expected query not in{expected_result}but got{context.driver.find.element(By.ID,'zg_banner_text')}"







