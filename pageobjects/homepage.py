from selenium.webdriver.common.by import By

from pageobjects.shoppage import ShopPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    email_textbox = (By.NAME, "email")
    password_textbox = (By.ID, "exampleInputPassword1")
    name_textbox = (By.CSS_SELECTOR, "input[name ='name']")
    submit_button = (By.XPATH, "//input[@type='submit']")
    dropdown_box = (By.ID, "exampleFormControlSelect1")
    option_selection = (By.CSS_SELECTOR, "input[value='option1']")
    success_message = (By.CLASS_NAME, "alert-success")

    def shop_item(self):
        self.driver.find_element(*HomePage.shop).click()
        shoppage = ShopPage(self.driver)
        return shoppage

    def  get_email_textbox(self):
        return self.driver.find_element(*HomePage.email_textbox)

    def get_password_textbox(self):
        return self.driver.find_element(*HomePage.password_textbox)

    def get_name_textbox(self):
        return self.driver.find_element(*HomePage.name_textbox)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_dropdown_box(self):
        return self.driver.find_element(*HomePage.dropdown_box)

    def get_option_selection(self):
        return self.driver.find_element(*HomePage.option_selection)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message)

