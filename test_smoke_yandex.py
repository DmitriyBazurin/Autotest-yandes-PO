from page.YandexPages import YandexMethods
from selenium import webdriver
import time



def test_yandex_search(browser):
    page = YandexMethods(browser)
    page.go_to_site()
    page.enter_word("Тензор")
    page.click_on_the_search_button()
    time.sleep(1)

def test_yandex_pictures(browser):
    driver = webdriver.Chrome
    page = YandexMethods(browser)
    page.go_to_site()
    page.click_on_the_pictures_button()

    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    get_url = page.get_current_url()
    assert 'yandex.ru/images' in get_url


    page.click_on_the_1st_pictures_img()

    page.click_on_the_1st_picture_yandex()
    time.sleep(1)
    pic1 = page.get_current_url()

    page.click_on_the_next_picture_yandex()

    page.click_on_the_prev_picture_yandex()
    time.sleep(1)
    pic2 = page.get_current_url()
    assert pic1 == pic2





    
