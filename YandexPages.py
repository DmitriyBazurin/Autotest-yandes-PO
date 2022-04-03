from .BaseApp import BasePage
from selenium.webdriver.common.by import By


class YandexMethods(BasePage):

    element_yandex_search_field = (By.ID, "text")
    element_yandex_search_button = (By.CLASS_NAME, "search2__button")
    element_yandex_pictures_button = (By.CSS_SELECTOR, "div.services-new__icon_images")
    element_img_page_1st_img = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    element_img_yandex_1st_img = (By.CSS_SELECTOR, '[role="list"] .serp-item_pos_0')
    element_prev_img_yandex = (By.CSS_SELECTOR, '.CircleButton_type_prev')
    element_next_img_yandex = (By.CSS_SELECTOR, '.CircleButton_type_next')

    def enter_word(self, word):
        search_field = self.find_element(self.element_yandex_search_field)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(self.element_yandex_search_button, time=2).click()

    def click_on_the_pictures_button(self):
        return self.find_element(self.element_yandex_pictures_button, time=2).click()
        
    def click_on_the_1st_pictures_img(self):
        return self.find_element(self.element_img_page_1st_img, time=2).click()

    def click_on_the_1st_picture_yandex(self):
        return self.find_element(self.element_img_yandex_1st_img, time=2).click()

    def click_on_the_next_picture_yandex(self):
        return self.find_element(self.element_next_img_yandex, time=2).click()

    def click_on_the_prev_picture_yandex(self):
        return self.find_element(self.element_prev_img_yandex, time=2).click()

   





