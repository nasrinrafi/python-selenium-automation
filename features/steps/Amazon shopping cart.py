from time import sleep
@given('open amazon page ')
def open_amazon(context):
  context.driver.get('https://www.amazon.com/')
  @when('click on shopping cart')
  def click_shoppingcart(context):
    context.driver.find_element(By.XPATH,'span[@class="nav-cart-icon nav-sprite').click()
    sleep(1)
