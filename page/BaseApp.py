from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://yandex.ru/"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_page_loaded(self, timeout=60, check_js_complete=True,
                         check_page_changes=False, check_images=True,
                         wait_for_element=None,
                         wait_for_xpath_to_disappear='',
                         sleep_time=2):
        # Эта функция ожидает, пока страница не будет полностью загружена.
        # Мы используем много различных способов определить, загружена страница или нет:
        # 1) Проверьте статус JS
        # 2) Проверьте изменение в исходном коде страницы
        # 3) Убедитесь, что все изображения загружены полностью
        # (Примечание: по умолчанию эта проверка отключена)
        # 4) Проверьте, что ожидаемые элементы представлены на странице


        page_loaded = False
        double_check = False
        k = 0

        if sleep_time:
            time.sleep(sleep_time)

        # Получить исходный код страницы для отслеживания изменений в HTML:

        source = ''
        try:
            source = self.driver.page_source
        except:
            pass

        # Дождитесь загрузки страницы (и прокрутите ее, чтобы убедиться, что все объекты будут загружены):
        while not page_loaded:
            time.sleep(0.5)
            k += 1

            if check_js_complete:
                # Прокрутите вниз и дождитесь загрузки страницы:
                try:
                    self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                    page_loaded = self.driver.execute_script("return document.readyState == 'complete';")
                except Exception as e:
                    pass

            if page_loaded and check_page_changes:
                # Проверьте, был ли изменен page source
                new_source = ''
                try:
                    new_source = self.driver.page_source
                except:
                    pass

                page_loaded = new_source == source
                source = new_source

            # Подождите, когда какой-нибудь элемент исчезнет:
            if page_loaded and wait_for_xpath_to_disappear:
                bad_element = None

                try:
                    bad_element = WebDriverWait(self.driver, 0.1).until(
                        EC.presence_of_element_located((By.XPATH, wait_for_xpath_to_disappear))
                    )
                except:
                    pass  # Игнорировать ошибки тайм-аута

                page_loaded = not bad_element

            if page_loaded and wait_for_element:
                try:
                    page_loaded = WebDriverWait(self.driver, 0.1).until(
                        EC.element_to_be_clickable(wait_for_element._locator)
                    )
                except:
                    pass  # Игнорировать ошибки тайм-аута

            assert k < timeout, 'The page loaded more than {0} seconds!'.format(timeout)

            # Проверьте два раза, что страница полностью загружена:
            if page_loaded and not double_check:
                page_loaded = False
                double_check = True

        # Go up:
        self.driver.execute_script('window.scrollTo(document.body.scrollHeight, 0);')
