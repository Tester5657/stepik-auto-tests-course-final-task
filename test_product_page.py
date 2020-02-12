from pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    product_price = page.get_product_price()
    product_name = page.get_product_name()
    page.click_add_to_busket_button()
    page.solve_quiz_and_get_code()
    page.should_have_correct_product_in_the_message(product_name)
    page.should_have_correct_price_in_the_message(product_price)
