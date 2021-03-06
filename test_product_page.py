import pytest
import faker

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True, scope="function")
    def setup(self, browser):
        login_page = LoginPage(browser, LoginPage.login_link)
        login_page.open()
        login_page.should_be_login_page()
        f = faker.Faker()
        email = f.email()
        login_page.register_new_user(email, "testtesttest")
        login_page.should_be_authorized_user()
        self.browser = browser
        yield
        # Logout
        browser.delete_all_cookies()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self):
        page = ProductPage(self.browser, ProductPage.product_link)
        page.open()
        page.should_not_be_success_message()
        product_price = page.get_product_price()
        product_name = page.get_product_name()
        page.click_add_to_bucket_button()
        page.should_have_correct_product_in_the_message(product_name)
        page.should_have_correct_price_in_the_message(product_price)

    def test_user_cant_see_success_message(self):
        page = ProductPage(self.browser, ProductPage.product_link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail(reason="fixing this bug right now")),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    browser.delete_all_cookies()
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    product_price = page.get_product_price()
    product_name = page.get_product_name()
    page.click_add_to_bucket_button()
    page.solve_quiz_and_get_code()
    page.should_have_correct_product_in_the_message(product_name)
    page.should_have_correct_price_in_the_message(product_price)


@pytest.mark.xfail()
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.click_add_to_bucket_button()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail()
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.click_add_to_bucket_button()
    page.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    browser.delete_all_cookies()
    page = ProductPage(browser, ProductPage.product_link)
    page.open()
    page.click_view_bucket_button()
    basked_page = BasketPage(browser, browser.current_url)
    basked_page.should_not_be_item_in_the_basket()
    basked_page.your_basket_is_empty_text_is_presented()
    basked_page.number_of_items_in_the_basket(0)
