from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexSeacrhLocators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH_BUTTON = (By.CLASS_NAME, "search2__button")
    LOCATOR_YANDEX_PICTURES_BUTTON = (By.CSS_SELECTOR, "div.services-new__icon_images")
    LOCATOR_YANDEX_1ST_IMG = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_BUTTON,time=2).click()

    def click_on_the_pictures_button(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_PICTURES_BUTTON,time=2).click()
        
    def click_on_the_1st_pictures(self):
        return self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_1ST_IMG,time=2).click()       
   





