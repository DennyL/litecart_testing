from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from test.config import URLs
from test.pages.base_page import BasePage


class MainPageLocators:

    """ Locators for the Main Page """

    page_url = URLs.url_main_page

    add_to_cart_button = (By.CSS_SELECTOR, 'button[name="add_cart_product"]')
    go_to_cart_button = (By.CSS_SELECTOR, 'div#cart a')
    cart_qty_badge = (By.CSS_SELECTOR, 'div#cart a .badge.quantity')
    cart_remove_item_button = (By.CSS_SELECTOR, '.item button[name="remove_cart_item"]')
    cart_is_empty_message = (By.XPATH, '//p[contains(text(),"There are no items in your cart.")]')

    @staticmethod
    def popular_products_locators(qty) -> list:
        """
            generates and returns a list of popular products locators in range of ids provided as a parameter
            :param qty: number of product locators to be returned
            :return: list of locators
        """
        locators_list = []
        for id_ in range(1, qty + 1):
            locators_list.append((By.CSS_SELECTOR, f'section#box-popular-products a.link[data-id="{str(id_)}"]'))
        return locators_list


class MainPage(BasePage, MainPageLocators):

    """ Methods to interact with the Main Page """

    def open(self):
        self.driver.get(self.page_url)

    def is_cart_qty_badge_number_grew(self, action):
        """
            decorator that wraps an action passed as a parameter.
            Checks the number displayed on the cart quantity badge before running the action.
            Waits till the number increased by 1
            :param action function to wrap
            :return :True if after running the action the quantity increased by 1, False otherwise
        """
        def wrapper(locator):
            qty_badge = self.driver.find_element(*self.cart_qty_badge)
            qty_before_action = int(qty_badge.text) if qty_badge.text != '' else 0
            WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(locator))
            action(locator)
            try:
                WebDriverWait(self.driver, 5).until(
                    ec.text_to_be_present_in_element(self.cart_qty_badge, str(qty_before_action + 1))
                )
            except (TimeoutException, NoSuchElementException):
                return False
            return True
        return wrapper

    @property
    def cart_badge_number(self) -> int:
        """
            :returns : a number displayed on the cart badge
        """
        qty_badge = self.driver.find_element(*self.cart_qty_badge)
        badge_number = int(qty_badge.text) if qty_badge.text != '' else 0
        return badge_number

    def open_the_cart(self):
        """ opens the cart by clicking on the cart icon """
        self.click_on(self.go_to_cart_button)

    def remove_all_items_in_cart(self):
        """
            removes all items from the cart by clicking on the Remove button against each item in there
        """
        while not self.driver.find_elements(*self.cart_is_empty_message):
            # click on the remove button till cart_is_empty_message appears
            try:
                self.click_on(self.cart_remove_item_button)
            except StaleElementReferenceException:
                continue
