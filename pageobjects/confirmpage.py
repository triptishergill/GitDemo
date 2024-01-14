from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country_selectbox = (By.XPATH, "//input[@id='country']")
    country_text = (By.XPATH, "//a[text()='India']")
    confirm_checkbox = (By.CSS_SELECTOR, ".checkbox.checkbox-primary label")
    purchase_button = (By.CSS_SELECTOR, "input[type='submit']")
    succcess_message = (By.CLASS_NAME, "alert-success")

    def get_country_selectbox(self):
        return self.driver.find_element(*ConfirmPage.country_selectbox)

    def get_country_text(self):
        return self.driver.find_element(*ConfirmPage.country_text)

    def get_confirm_checkbox(self):
        return self.driver.find_element(*ConfirmPage.confirm_checkbox)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def get_succcess_message(self):
        return self.driver.find_element(*ConfirmPage.succcess_message)