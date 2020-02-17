from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def no_products_in_basket(self):
        pass

    def your_basket_is_empty_text_is_presented(self):
        assert self.is_element_present(*BasketPageLocators.YOUR_BASKET_IS_EMPTY), \
            "the message 'your backed is empty' is not presented"
        message = self.browser.find_element(*BasketPageLocators.YOUR_BASKET_IS_EMPTY)
        assert message.text == "Your basket is empty. Continue shopping"

    def number_of_items_in_the_basket(self, expected_number_of_items):
        items_in_the_basket = self.browser.find_elements(*BasketPageLocators.ITEMS_IN_THE_BASKET)
        assert len(items_in_the_basket) == expected_number_of_items

    def should_not_be_item_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_IN_THE_BASKET), "Basket is not empty"
