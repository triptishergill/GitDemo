import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def get_logger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # filehander object
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_presence(self, text):
        element = (WebDriverWait(self.driver, 20).until
                   (expected_conditions.presence_of_element_located((By.LINK_TEXT, text))))
        return element

    def verify_elements_visibility(self, locator):
        elements = (WebDriverWait(self.driver, 20).until(
            expected_conditions.visibility_of_all_elements_located
            (locator)))
        return elements

    def verify_element_presence(self, locator):
        element = (WebDriverWait(self.driver, 20).until
                   (expected_conditions.presence_of_element_located(locator)))
        return element

    def verify_element_clickable(self, locator):
        element = (WebDriverWait(self.driver, 20).until(
            expected_conditions.element_to_be_clickable(locator)))
        return element

    def select_bytext(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)


    def select_byindex(self, locator, index):
        dropdown = Select(locator)
        dropdown.select_by_index(index)
