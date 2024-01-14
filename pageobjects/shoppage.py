from selenium.webdriver.common.by import By

from pageobjects.confirmpage import ConfirmPage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    card_title = (By.XPATH, "//div[@class='card h-100']")
    card_text = (By.XPATH, "div/h4/a")
    card_button = (By.XPATH, "div/button")
    confirm_button = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkout_button = (By.CSS_SELECTOR, "button[class*='success']")

    def get_card_text(self):
        return self.driver.find_element(*ShopPage.card_text)

    def get_card_button(self):
        return self.driver.find_element(*ShopPage.card_button)

    def get_confirm_button(self):
        return self.driver.find_element(*ShopPage.confirm_button)

    def get_checkout_button(self):
        self.driver.find_element(*ShopPage.checkout_button).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage
