from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.events import EventFiringWebDriver
from test.listeners import listeners


class URLs:
    """
        Contains URLs and endpoints for the product
    """
    base_url = 'http://127.0.0.1/litecart'

    # ENDPOINTS
    main_page_endpoint = '/'
    admin_page_endpoint = '/admin/'

    # Joint URLs (base urls with endpoints)
    url_main_page = base_url + main_page_endpoint
    url_admin_page = base_url + admin_page_endpoint


class Links:
    """
        Contains links to different file resources required by this testing framework
    """
    LINK_TO_IMAGES_FOLDER = 'test/testdata/images'


class Credentials:
    """
        Contains credentials required to fulfill actions on behalf of different kinds of users
    """
    admin_credentials = (
        {'username': 'admin', 'password': 'admin'},
    )


class Browser:
    """
        A browser selection, wrapping and instantiation
    """
    def __init__(self, with_browser='chrome'):
        if with_browser.lower() == 'chrome':
            self.plain_driver = webdriver.Chrome(ChromeDriverManager().install())
        elif with_browser.lower() == 'opera':
            self.plain_driver = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            raise Exception('Browser name is not defined')

        self.event_driver = EventFiringWebDriver(self.plain_driver, listeners.FindAndClickListener())

        self.driver = self.plain_driver
        # in case you need an event driver with event listeners,
        # to switch to an event driver
        # UNCOMMENT THE LINE BELOW:
        # self.driver = self.event_driver
        self.driver.maximize_window()

    def destroy_and_quit(self):
        self.driver.quit()
