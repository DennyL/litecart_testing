from selenium.webdriver.common.by import By
from test.pages.base_page import BasePage
from test.config import URLs


class AdminPageLocators:

    """ Locators for the Admin Page """

    page_url = URLs.url_admin_page

    login_box = (By.CSS_SELECTOR, 'input.form-control[name=username]')
    password_box = (By.CSS_SELECTOR, 'input.form-control[name=password]')
    login_button = (By.CSS_SELECTOR, 'button[name=login]')

    header_for_all_pages = (By.CSS_SELECTOR, 'div.panel-heading')

    ### LEFT SIDE-MENU ITEMS ###
    left_side_menu_items_locators = (
        {'Appearance main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=appearance]')},
        {'Appearance/Template': (By.CSS_SELECTOR, 'li.doc[data-code=template]')},
        {'Appearance/Logotype': (By.CSS_SELECTOR, 'li.doc[data-code=logotype]')},
        {'Catalog main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=catalog]')},
        {'Catalog/Catalog': (By.CSS_SELECTOR, 'li.doc[data-code=catalog]')},
        {'Catalog/Attribute Groups': (By.CSS_SELECTOR, 'li.doc[data-code=attribute_groups]')},
        {'Catalog/Manufactures': (By.CSS_SELECTOR, 'li.doc[data-code=manufacturers]')},
        {'Catalog/Suppliers': (By.CSS_SELECTOR, 'li.doc[data-code=suppliers]')},
        {'Catalog/Delivery Statuses': (By.CSS_SELECTOR, 'li.doc[data-code=delivery_statuses]')},
        {'Catalog/Sold Out Statuses': (By.CSS_SELECTOR, 'li.doc[data-code=sold_out_statuses]')},
        {'Catalog/Quantity Units': (By.CSS_SELECTOR, 'li.doc[data-code=quantity_units]')},
        {'Catalog/CSV Import/Export': (By.CSS_SELECTOR, 'li.doc[data-code=csv]')},
        {'Countries main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=countries]')},
        {'Currencies main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=currencies]')},
        {'Customers main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=customers]')},
        {'Customers/Customers': (By.CSS_SELECTOR, 'li.doc[data-code=customers]')},
        {'Customers/CSV Import/Export': (By.CSS_SELECTOR, 'li.doc[data-code=csv]')},
        {'Customers/Newsletter': (By.CSS_SELECTOR, 'li.doc[data-code=newsletter]')},
        {'Geo Zones main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=geo_zones]')},
        {'Languages main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=languages]')},
        {'Languages/Languages': (By.CSS_SELECTOR, 'li.doc[data-code=languages]')},
        {'Languages/Storage Encoding': (By.CSS_SELECTOR, 'li.doc[data-code=storage_encoding]')},
        {'Modules main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=modules]')},
        {'Modules/Customer Modules': (By.CSS_SELECTOR, 'li.doc[data-code=customer]')},
        {'Modules/Shipping Modules': (By.CSS_SELECTOR, 'li.doc[data-code=shipping]')},
        {'Modules/Payment Modules': (By.CSS_SELECTOR, 'li.doc[data-code=payment]')},
        {'Modules/Order Modules': (By.CSS_SELECTOR, 'li.doc[data-code=order]')},
        {'Modules/Order Total Modules': (By.CSS_SELECTOR, 'li.doc[data-code=order_total]')},
        {'Modules/Job Modules': (By.CSS_SELECTOR, 'li.doc[data-code=jobs]')},
        {'Orders main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=orders]')},
        {'Orders/Orders': (By.CSS_SELECTOR, 'li.doc[data-code=orders]')},
        {'Orders/Order Statuses': (By.CSS_SELECTOR, 'li.doc[data-code=order_statuses]')},
        {'Pages main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=pages]')},
        {'Pages/Pages': (By.CSS_SELECTOR, 'li.doc[data-code=pages]')},
        {'Pages/CSV Import/Export': (By.CSS_SELECTOR, 'li.doc[data-code=csv]')},
        {'Reports main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=reports]')},
        {'Reports/Monthly Sales': (By.CSS_SELECTOR, 'li.doc[data-code=monthly_sales]')},
        {'Reports/Most Sold Products': (By.CSS_SELECTOR, 'li.doc[data-code=most_sold_products]')},
        {'Reports/Most Shopping Customers': (By.CSS_SELECTOR, 'li.doc[data-code=most_shopping_customers]')},
        {'Settings main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=settings]')},
        {'Settings/Store Info': (By.CSS_SELECTOR, 'li.doc[data-code=store_info]')},
        {'Settings/Defaults': (By.CSS_SELECTOR, 'li.doc[data-code=defaults]')},
        {'Settings/Email': (By.CSS_SELECTOR, 'li.doc[data-code=email]')},
        {'Settings/Listings': (By.CSS_SELECTOR, 'li.doc[data-code=listings]')},
        {'Settings/Customer Details': (By.CSS_SELECTOR, 'li.doc[data-code=customer_details]')},
        {'Settings/Legal': (By.CSS_SELECTOR, 'li.doc[data-code=legal]')},
        {'Settings/Images': (By.CSS_SELECTOR, 'li.doc[data-code=images]')},
        {'Settings/Checkout': (By.CSS_SELECTOR, 'li.doc[data-code=checkout]')},
        {'Settings/Advanced': (By.CSS_SELECTOR, 'li.doc[data-code=advanced]')},
        {'Settings/Security': (By.CSS_SELECTOR, 'li.doc[data-code=security]')},
        {'Slides main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=slides]')},
        {'Tax main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=tax]')},
        {'Tax/Tax Rates': (By.CSS_SELECTOR, 'li.doc[data-code=tax_rates]')},
        {'Tax/Tax Classes': (By.CSS_SELECTOR, 'li.doc[data-code=tax_classes]')},
        {'Translations main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=translations]')},
        {'Translations/Search': (By.CSS_SELECTOR, 'li.doc[data-code=search]')},
        {'Translations/Scan Files': (By.CSS_SELECTOR, 'li.doc[data-code=scan]')},
        {'Translations/CSV Import/Export': (By.CSS_SELECTOR, 'li.doc[data-code=csv]')},
        {'Users main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=users]')},
        {'vQmods main': (By.CSS_SELECTOR, 'ul#box-apps-menu li.app[data-code=vqmods]')},
    )


class AdminPage(BasePage, AdminPageLocators):
    """ Methods to interact with the Admin Page """

    def open(self):
        """ Opens the Admin Page """
        self.driver.get(self.page_url)

    def login_with(self, credentials: dict):
        """ logs in to the on the admin page with the credentials provided as the parameters
            :param credentials: dict with keys {'username'} and {'password'}
        """
        self.driver.find_element(*self.login_box).send_keys(credentials['username'])
        self.driver.find_element(*self.password_box).send_keys(credentials['password'])
        self.driver.find_element(*self.login_button).click()
