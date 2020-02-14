from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_bucket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_have_correct_product_in_the_message(self, product_name):
        product_name_in_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_THE_SUCCESS_MESSAGE)
        assert product_name == product_name_in_the_message.text, \
            "Incorrect product name in the message"

    def should_have_correct_price_in_the_message(self, product_price):
        product_price_in_the_message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_THE_SUCCESS_MESSAGE)
        assert product_price == product_price_in_the_message.text, \
            "Incorrect product price in the message"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message should disappear"
