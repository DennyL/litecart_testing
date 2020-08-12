from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from test.pages.base_page import BasePage, BasePageLocators


class CountriesPageLocators(BasePageLocators):

    first_country_in_the_list = (By.XPATH, '//tbody/tr/td[5]/a')

    in_country_external_links_locators = (
        {'ISO 3166-1 numeric': (By.XPATH, '//*[@class="form-group col-md-6 required"]/label[contains(text(),"Number")]/a')},
        {'ISO 3166-1 alpha-2': (By.XPATH, '//*[@class="form-group col-md-6 required"]/label[contains(text(),"alpha-2")]/a')},
        {'ISO 3166-1 alpha-3': (By.XPATH, '//*[@class="form-group col-md-6 required"]/label[contains(text(),"alpha-3")]/a')},
        {'Address Format': (By.XPATH, '//*[@class="form-group"]/label[contains(text(), "Address")]/a[@target="_blank"]')},
        {'Tax ID Format': (By.XPATH, '//*[@class="form-group col-md-6"]/label[contains(text(), "Tax")]/a')},
        {'Postcode Format': (By.XPATH, '//*[@class="form-group col-md-6"]/label[contains(text(), "Post")]/a')},
        {'Language Code': (By.XPATH, '//*[@class="form-group col-md-4"]/label[contains(text(), "Language")]/a')},
        {'Currency Code': (By.XPATH, '//*[@class="form-group col-md-4"]/label[contains(text(), "Currency")]/a')},
        {'Phone Country Code': (By.XPATH, '//*[@class="form-group col-md-4"]/label[contains(text(), "Phone Country")]/a')},
    )


class CountriesPage(BasePage, CountriesPageLocators):

    """ Methods to interact with the Countries Page """

    def open(self):
        """ opens the Countries page from Admin page. Admin page has to be opened beforehand """
        page_locator = (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=countries]')
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(page_locator))
        self.driver.find_element(*page_locator).click()
