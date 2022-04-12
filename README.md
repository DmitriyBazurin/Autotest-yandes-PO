# Tensor
 tensor homework

тестовое задание реализовано с использованием Python Selenium+PyTest
Файл с тестом - test_smoke_yandex.py
в папке page находятся: BaseApp.py - базовые методы для работы с Webdriver
                        YandexTest.py - класс c методами и элементами для веб-страницы
в файле conftest.py находится фикстура для запуска и закрытия браузера
    с возможностью выбора браузера(--browser_name=chrome or firefox)
команда запуска теста: pytest -v test_smoke_yandex.py
    
