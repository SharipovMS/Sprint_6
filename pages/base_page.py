from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

'''
Этот класс не описывает конкретную страницу
класс хранит в себе "общие" методы - действия
на странице.
'''

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, locator):
        return self.browser.find_element(*locator)

    def find_elements(self, locator):
        return self.browser.find_elements(*locator)

    def click_button(self, locator):
        button = self.browser.find_element(*locator)
        button.click()

    def get_element_text(self, locator):
        element = self.browser.find_element(*locator)
        return element.text

    def scroll_to_element(self, locator):
        element = self.browser.find_element(*locator)
        self.browser.execute_script("arguments[0].scrollIntoView();", element)

    def element_is_visible(self, locator):
        return WebDriverWait(self.browser, 5).until(expected_conditions.visibility_of_element_located(locator))

    def switch_to_window(self):
        return self.browser.switch_to.window(self.browser.window_handles[-1])

    def fill_field(self, locator, value):
        element = self.browser.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def wait_for_site(self, url):
        WebDriverWait(self.browser, 5).until(expected_conditions.url_to_be(url))

    def current_get_url(self):
        return self.browser.current_url


