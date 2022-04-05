from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url


