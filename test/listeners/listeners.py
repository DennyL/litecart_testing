from selenium.webdriver.support.events import AbstractEventListener


class FindAndClickListener(AbstractEventListener):

    def __init__(self):
        super().__init__()
        self.clicked_element_name = None

    def before_find(self, by, value, driver):
        print(f'[Starting search for element]: >>> {value} <<<')

    def after_find(self, by, value, driver):
        print(f'[Element has been found]: >>> {value} <<<')

    def before_click(self, element, driver):
        self.clicked_element_name = element.text
        print(f'[Clicking on element]: >>> {self.clicked_element_name} <<<')

    def after_click(self, element, driver):
        print(f'[Element has been clicked]: >>> {self.clicked_element_name} <<<')

    def on_exception(self, exception, driver):
        print(f'[ISSUE FOUND]: !!! {exception} !!!')
