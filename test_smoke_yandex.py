from page.YandexPages import YandexMethods
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select




def test_yandex_search(browser):
    page = YandexMethods(browser)
    page.go_to_site()
    page.enter_word("Тензор")
    time.sleep(1)
    page.enter_word(Keys.DOWN)
    time.sleep(2)
    assert page.find_suggest_list()
    page.enter_word(Keys.ENTER)
    time.sleep(2)
    page.click_on_the_search_button()
    time.sleep(1)
    assert page.find_href_tensor()


def test_yandex_pictures(browser):
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







    
