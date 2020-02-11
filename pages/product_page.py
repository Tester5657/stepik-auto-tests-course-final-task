from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def click_add_to_busket_button(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def message_product_was_added_in_the_busket_should_appear(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_PRODUCT_WAS_ADDED_TO_BUSKET)
        assert product_name.text in message.text, "Incorrect product name in the message"

    def message_your_busket_total_price_should_appear(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_YOUR_BASKET_TOTAL_IS_NOW)
        assert product_price.text in message.text, "Incorrect product price in the message"
