from time import sleep


def highlight_element(element, driver, highlight_time=.3):

    """ Highlights an element on the webpage by applying styles to it """

    def apply_style(style):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, style)
    original_style = element.get_attribute('style')

    apply_style("background: light gray; border: 2px solid orange;")
    sleep(highlight_time)
    apply_style(original_style)
