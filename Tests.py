from .YandexPages import YandexMethods
import time


def test_yandex_search(browser):
    yandex_main_page = YandexMethods(browser)
    yandex_main_page.go_to_site()

    yandex_main_page.enter_word("Тензор")

    yandex_main_page.click_on_the_search_button()
    time.sleep(1)
    

def test_yandex_pictures(browser):
    yandex_main_page = YandexMethods(browser)
    yandex_main_page.go_to_site()
    time.sleep(1)
    yandex_main_page.click_on_the_pictures_button()
    time.sleep(1) 

    tabs = browser.window_handles
    browser.switch_to.window(tabs[1]) 

    yandex_main_page.click_on_the_1st_pictures_img()
    time.sleep(1)

    yandex_main_page.click_on_the_1st_picture_yandex()
    pic1 = browser.current_url
    time.sleep(1)

    yandex_main_page.click_on_the_next_picture_yandex()
    time.sleep(1)

    yandex_main_page.click_on_the_prev_picture_yandex()
    pic2 = browser.current_url
    assert pic1 == pic2
    time.sleep(1)




    
