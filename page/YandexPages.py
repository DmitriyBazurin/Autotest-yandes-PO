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
    element_yandex_1st_suggest = (By.CSS_SELECTOR, '.mini-suggest__item[data-index="1"]')
    element_href_tensor = (By.CSS_SELECTOR, '[href="https://tensor.ru/"]')

    # elements_yandex_search_result = (By.CSS_SELECTOR, '#search-result [accesskey]')





    def go_to_site(self):
        self.base_url = "https://yandex.ru/"
        return self.driver.get(self.base_url)

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

    def find_suggest_list(self):
        return self.find_element(self.element_yandex_1st_suggest, time=2)

    def find_href_tensor(self):
        return self.find_element(self.element_href_tensor, time=2)




    # def get_search_elements_list(self):
    #     elements = self.find_elements(self.elements_yandex_search_result, time=2)
    #     for elem in elements:


    # def get_href(self):
    #     elems = self.find_element(".sc-eYdvao.kvdWiq [href]")
    #     links = [elem.get_attribute('href') for elem in elems]























