from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def should_be_in_basket(self):
        self.add_to_basket()
        self.should_match_with_title()
        self.should_match_with_cost()
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
    def should_match_with_title(self):
        title_in_message = self.browser.find_element(*ProductPageLocators.TITLE_IN_MESSAGE).text
        real_title = self.browser.find_element(*ProductPageLocators.REAL_TITLE).text
        assert title_in_message==real_title, "Title doesn't match"
    def should_match_with_cost(self):
        cost_in_message = self.browser.find_element(*ProductPageLocators.COST_IN_MESSAGE).text
        real_cost = self.browser.find_element(*ProductPageLocators.REAL_COST).text
        print(f"answer: {real_cost}")
        assert cost_in_message==real_cost, "Cost doesn't match"