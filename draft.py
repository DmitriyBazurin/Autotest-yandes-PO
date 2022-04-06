from selenium import webdriver


def get_attributes(driver, element) -> dict:
    return driver.execute_script(
        """
        let attr = arguments[0].attributes;
        let items = {}; 
        for (let i = 0; i < attr.length; i++) {
            items[attr[i].name] = attr[i].value;
        }
        return items;
        """,
        element
    )


driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds
driver.get('https://yandex.ru/')


input_el = driver.find_element_by_id('text')
attrs = get_attributes(driver, input_el)
print(attrs)

elems = driver.find_elements_by_css_selector("[accesskey]")
for elem in elems:
    print(elem.get_attribute("href"))

driver.quit()



