import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()