import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.homepage import HomePage
from testdata.homepagedata import HomePageData
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, getdata):
        log = self.get_logger()
        homepage = HomePage(self.driver)
        log.info("Email is"+ getdata["email"])
        homepage.get_email_textbox().send_keys(getdata["email"])
        homepage.get_password_textbox().send_keys(getdata["password"])
        homepage.get_name_textbox().send_keys(getdata["name"])
        homepage.get_submit_button().click()
        self.select_bytext(homepage.get_dropdown_box(), getdata["gender"])
        homepage.get_option_selection().click()
        success_text = homepage.get_success_message().text

        print(success_text)
        assert "Success" in success_text
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getdata(self, request):
        return request.param
