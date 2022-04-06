from page.YandexTest import YandexTest
import time
from selenium.webdriver.common.keys import Keys

def test_yandex_search(browser):
    page = YandexTest(browser)
    page.go_to_site()
    page.enter_word("Тензор")
    page.enter_word(Keys.DOWN)
    # проверка наличия элемента suggest
    page.screenshot()
    assert page.find_suggest_list()
    page.enter_word(Keys.ENTER)
    page.screenshot()
    # проверка наличия эелемента с адресом "https://tensor.ru/"
    assert page.find_href_tensor()

def test_yandex_pictures(browser):
    page = YandexTest(browser)
    page.go_to_site()
    page.click_on_the_pictures_button()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    get_url = page.get_current_url()
    page.screenshot()
    # проверка перехода по адресу yandex.ru/images
    assert 'yandex.ru/images' in get_url
    page.click_on_the_1st_pictures_img()
    page.click_on_the_1st_picture_yandex()
    time.sleep(1)
    pic1 = page.get_current_url()
    page.click_on_the_next_picture_yandex()
    page.click_on_the_prev_picture_yandex()
    time.sleep(1)
    pic2 = page.get_current_url()
    page.screenshot()
    # проверка возврата на прошлый адрес
    assert pic1 == pic2







    
