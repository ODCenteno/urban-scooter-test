from selenium.webdriver.common.by import By

class PageActions:

    def __init__(self, driver) -> None:
        self.driver = driver

    def click(self, selector):
        self.driver.find_element(*selector).click()

    def type_text(self, selector, text):
        self.driver.find_element(*selector).send_keys(text)

    def get_text(self, selector):
        return self.driver.find_element(*selector).text

    def get_property_value(self, selector, prop):
        return self.driver.find_element(*selector).get_property(prop)

