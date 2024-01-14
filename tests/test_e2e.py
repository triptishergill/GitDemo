from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time

from pageobjects.homepage import HomePage
from pageobjects.shoppage import ShopPage
from utilities.baseclass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.get_logger()
        self.driver.implicitly_wait(4)
        homepage = HomePage(self.driver)
        log.info("Getting all the card titles")
        shoppage = homepage.shop_item()
        items = self.verify_elements_visibility(shoppage.card_title)
        for item in items:
            name = item.find_element(By.XPATH, "div/h4/a").text
            log.info(name)
            if name == "Blackberry":
                print(name)
                item.find_element(By.XPATH, "div/button").click()

        self.verify_element_presence(shoppage.confirm_button)
        shoppage.get_confirm_button().click()
        log.info("Entering country name as ind")
        confirmpage = shoppage.get_checkout_button()
        confirmpage.get_country_selectbox().send_keys("ind")
        self.verify_link_presence("India")
        confirmpage.get_country_text().click()
        self.verify_element_clickable(confirmpage.get_confirm_checkbox())
        confirmpage.get_confirm_checkbox().click()
        confirmpage.get_purchase_button().click()
        message = confirmpage.get_succcess_message().text
        log.info(message)
        assert "Success! Thank you1!" in message
        print("success")
