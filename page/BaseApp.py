from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        driver.implicitly_wait(10)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def get_current_url(self):
        return self.driver.current_url

    def get(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)

    # def get_href(self):
    #     elems = self.driver.find_elements_by_css_selector(".sc-eYdvao.kvdWiq [href]")
    #     links = [elem.get_attribute('href') for elem in elems]

    def refresh(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    # def screenshot(self, file_name='screenshot.png'):
    #     self.driver.save_screenshot(file_name)












