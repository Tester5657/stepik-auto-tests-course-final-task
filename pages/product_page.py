from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_busket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_have_correct_product_in_the_message(self, product_name):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED_TO_BUSKET)
        assert product_name in message.text, "Incorrect product name in the message"

    def should_have_correct_price_in_the_message(self, product_price):
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_YOUR_BASKET_TOTAL_IS_NOW)
        assert product_price in message.text, "Incorrect product price in the message"

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text