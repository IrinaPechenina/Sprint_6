from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @staticmethod
    def format_locator(locator, num):
        method, locator = locator
        locator = locator.format(num)
        return method, locator

    def switch_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
