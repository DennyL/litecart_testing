from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from test.pages.base_page import BasePage
from test.testdata.testdata import Product


class CatalogPageLocators:

    catalog_page_main = (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=catalog]')
    catalog_subpage = (By.CSS_SELECTOR, 'li.doc[data-code=catalog]')

    add_new_product_button = (By.XPATH, '//ul[@class="list-inline"]//li[2]/a')
    add_new_category_button = (By.XPATH, '//ul[@class="list-inline"]//li[1]/a')
    select_all_products_checkbox = (By.CSS_SELECTOR, 'i[data-toggle="checkbox-toggle"]')
    search_box = (By.CSS_SELECTOR, 'input.form-control[data-type="search"][placeholder="Search phrase or keyword"]')
    search_button = (By.CSS_SELECTOR, 'button[value="Search"]')
    save_new_product_button = (By.CSS_SELECTOR, 'button[value="Save"]')
    delete_button = (By.CSS_SELECTOR, 'button[value="Delete"]')

    ### Add New Product subpage locators ###
    # GENERAL
    general_tab = (By.XPATH, '//a[contains(text(), "General")]')
    general_name = (By.CSS_SELECTOR, 'input.form-control[name="name[en]"]')
    general_code = (By.CSS_SELECTOR, 'input.form-control[name="code"]')
    general_sku = (By.CSS_SELECTOR, 'input.form-control[name="sku"]')
    general_mpn = (By.CSS_SELECTOR, 'input.form-control[name="mpn"]')
    general_gtin = (By.CSS_SELECTOR, 'input.form-control[name="gtin"]')
    general_taric = (By.CSS_SELECTOR, 'input.form-control[name="taric"]')
    general_manufacturer_select = (By.CSS_SELECTOR, 'select[name="manufacturer_id"]')
    general_date_valid_from = (By.CSS_SELECTOR, 'input[name="date_valid_from"]')
    general_date_valid_to = (By.CSS_SELECTOR, 'input[name="date_valid_to"]')
    general_keywords = (By.CSS_SELECTOR, 'input[name="keywords"]')
    general_input_product_images = (By.CSS_SELECTOR, 'input.form-control[name="new_images[]"]')
    # INFORMATION
    information_tab = (By.XPATH, '//a[contains(text(), "Information")]')
    information_short_description = (By.CSS_SELECTOR, 'input.form-control[name="short_description[en]"]')
    information_description = (By.CSS_SELECTOR, '.trumbowyg-editor')
    information_technical_data = (By.CSS_SELECTOR, 'textarea[name="technical_data[en]"]')
    information_head_title = (By.CSS_SELECTOR, 'input[name="head_title[en]"]')
    information_meta_description = (By.CSS_SELECTOR, 'input[name="meta_description[en]"]')
    # PRICES
    prices_tab = (By.XPATH, '//a[contains(text(), "Prices")]')
    prices_tax_class = (By.CSS_SELECTOR, 'select[name="purchase_price_currency_code"]')
    prices_purchase_price = (By.CSS_SELECTOR, 'input[name="purchase_price"]')
    prices_purchase_price_currency_code_select = (By.CSS_SELECTOR, 'select[name="purchase_price_currency_code"]')
    prices_price_usd = (By.CSS_SELECTOR, 'input.form-control[name="prices[USD]"]')


class CatalogPage(BasePage, CatalogPageLocators):

    """ Methods to interact with the Catalog Page """

    def open(self):
        """
            Opens the Catalog page from Admin page.
            Admin page has to be opened beforehand
        """
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(self.catalog_page_main))
        catalog_li = self.driver.find_element(*self.catalog_page_main)
        catalog_li.click()

    def upload_product_image(self, abs_path_to_image: str):
        """
            :param : str, absolute path to an image
            sends an absolute path to an image to the application uploader
        """
        self.driver.find_element(*self.general_input_product_images).send_keys(abs_path_to_image)

    def fill_out_general_tab(self, product):
        """
            fills out required fields in the Catalog -> New Product Creation -> tab General
            :param product: an instance of a Product class from testdata/testdata
        """
        self.driver.find_element(*self.general_tab).click()
        self.driver.find_element(*self.general_code).send_keys(product.code)
        self.driver.find_element(*self.general_sku).send_keys(product.sku)
        self.driver.find_element(*self.general_mpn).send_keys(product.mpn)
        self.driver.find_element(*self.general_gtin).send_keys(product.gtin)
        self.driver.find_element(*self.general_taric).send_keys(product.taric)
        self.driver.find_element(*self.general_name).send_keys(product.product_name)
        manufacturer_selector = Select(self.driver.find_element(*self.general_manufacturer_select))
        manufacturer_selector.select_by_value(product.manufacturer)
        self.driver.find_element(*self.general_date_valid_from).send_keys(product.date_valid_from)
        self.driver.find_element(*self.general_date_valid_to).send_keys(product.date_valid_to)
        self.driver.find_element(*self.general_keywords).send_keys(product.keywords)
        self.upload_product_image(product.image)

    def fill_out_information_tab(self, product):
        """
            fills out required fields in the Catalog -> New Product Creation -> tab Information
            :param product: an instance of a Product class from testdata/testdata
        """
        self.driver.find_element(*self.information_tab).click()
        self.driver.find_element(*self.information_short_description).send_keys(product.short_description)
        self.driver.find_element(*self.information_description).send_keys(product.description)
        self.driver.find_element(*self.information_technical_data).send_keys(product.technical_data)
        self.driver.find_element(*self.information_head_title).send_keys(product.head_title)
        self.driver.find_element(*self.information_meta_description).send_keys(product.meta_description)

    def fill_out_prices_tab(self, product):
        """
            fills out required fields in the Catalog -> New Product Creation -> tab Prices
            :param product: an instance of a Product class from testdata/testdata
        """
        self.driver.find_element(*self.prices_tab).click()
        self.driver.find_element(*self.prices_purchase_price).send_keys(product.purchase_price)
        currency_selector = Select(self.driver.find_element(*self.prices_purchase_price_currency_code_select))
        currency_selector.select_by_value(product.purchase_price_currency)
        self.driver.find_element(*self.prices_price_usd).send_keys(product.price_usd)

    def create_product(self) -> str:
        """ creates a product in the LiteCart shop by instantiation of the Product class
            and filling the forms in the app with the fields of that instance.
            :returns : name of the product created, so that it could be traced
        """
        product = Product()
        self.fill_out_general_tab(product)
        self.fill_out_information_tab(product)
        self.fill_out_prices_tab(product)
        self.click_on(self.save_new_product_button)
        return product.product_name

    def is_product_in_the_root_catalog(self, name: str) -> bool:
        """
            Verifies if a product item with the name passed as a parameter present in the Root products list
            in the Catalog/Catalog page
            :param name: a str the product name is being consisted with
            :return: True if an element with the name given is present, False otherwise
        """
        self.driver.find_element(*self.catalog_subpage).click()
        product_locator = (By.XPATH, f'//a[contains(text(), {name})]')
        try:
            self.driver.find_element(*product_locator)
        except NoSuchElementException:
            return False
        return True

    def remove_created_products_from_catalog(self, keyword='item'):
        """
            Removes all items from Catalog/Catalog page found by the keyword
            passed as the parameter
            :param keyword: to find items by. Set to 'item' by default,
            since the items created by this framework are configured to start with 'item_' word
            in the generators/item_names_generator()
        """
        self.driver.find_element(*self.catalog_subpage).click()
        WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.search_box))
        self.driver.find_element(*self.search_box).send_keys(keyword)
        self.driver.find_element(*self.search_button).click()
        self.driver.find_element(*self.select_all_products_checkbox).click()
        self.driver.find_element(*self.delete_button).click()
        alert = self.driver.switch_to.alert
        alert.accept()
        # the following step (switch to the Catalog page) was added
        # to let the server a few milliseconds to apply items removal,
        # because without that server sometimes does not have time to accept the change
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(self.catalog_subpage))
        self.driver.find_element(*self.catalog_subpage).click()
