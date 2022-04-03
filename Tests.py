from .YandexPages import SearchHelper
import time


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    time.sleep(1)
    yandex_main_page.enter_word("Тензор")
    time.sleep(1)
    yandex_main_page.click_on_the_search_button()
    time.sleep(1)
    

def test_yandex_pictures(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site()
    time.sleep(1)
    yandex_main_page.click_on_the_pictures_button()
    time.sleep(1) 

    tabs = browser.window_handles
    browser.switch_to.window(tabs[1]) 

    yandex_main_page.click_on_the_1st_pictures()
    time.sleep(1)  
    
