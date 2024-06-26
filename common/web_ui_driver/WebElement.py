# from poium import Element as poium_Element
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import NoSuchElementException
# from appium.webdriver.common.appiumby import AppiumBy
# from poium.common.exceptions import FindElementTypesError
# from poium.common import logging
# from func_timeout.exceptions import FunctionTimedOut
# from poium.config import Browser

from poium.base_page import Element as poium_Element, Elements
from loguru import logger as logging
from poium.config import Browser


class WebElement(poium_Element):

    @property
    def attribute_value(self):
        return self.get_attribute('value')

    # def __get_element(self, by: str, value: str):
    #     """
    #     Judge element positioning way, and returns the element.
    #     """
    #
    #     if by in BY_LIST:
    #         elem = self.find(by, value)
    #         if len(elem) == 0:
    #             self.exist = False
    #             return None
    #         else:
    #             self.exist = True
    #             elem = elem[self.index]
    #     else:
    #         raise FindElementTypesError("Please enter the correct targeting elements")
    #
    #     if Browser.show is True:
    #         try:
    #             style_red = 'arguments[0].style.border="2px solid #FF0000"'
    #             style_blue = 'arguments[0].style.border="2px solid #00FF00"'
    #             style_null = 'arguments[0].style.border=""'
    #
    #             for _ in range(2):
    #                 self.driver.execute_script(style_red, elem)
    #                 sleep(0.1)
    #                 self.driver.execute_script(style_blue, elem)
    #                 sleep(0.1)
    #             self.driver.execute_script(style_blue, elem)
    #             sleep(0.5)
    #             self.driver.execute_script(style_null, elem)
    #         except WebDriverException:
    #             pass
    #
    #     return elem

    def js_click(self) -> None:
        """
        JS Clicks the element.
        """
        elem = self.get_element_object()
        self.driver.execute_script("arguments[0].click();", elem)
        logging.info(f"✅ js_click().")

    def is_exist_in_times(self, seconds: int = 120, raise_msg: str = "", expected_exist: bool = True) -> bool:
        """
        :param seconds:
        :param raise_msg:
        :param expected_exist:
        :return: match expected will return Ture
        """
        temp = self.times
        self.times = 1
        for i in range(int(seconds / 2)):
            temp = self.is_exist()
            self.is_exist()
            logging.debug(f'{self.desc} existing is {temp}')
            if temp == expected_exist:
                self.times = temp
                return True

        self.times = temp
        if raise_msg:
            raise TimeoutError(f'{seconds}s - {raise_msg}')
        return False

    def is_enable_in_times(self, seconds: int = 120, raise_msg: str = "", expected_exist: bool = True) -> bool:
        """
        :param seconds:
        :param raise_msg:
        :param expected_exist:
        :return: match expected will return Ture
        """
        temp = self.times
        self.times = 1
        for i in range(int(seconds / 2)):
            temp = self.is_enabled()
            logging.debug(f'{self.desc} existing is {temp}')
            if temp == expected_exist:
                self.times = temp
                return True
        self.times = temp
        if raise_msg:
            raise TimeoutError(f'{seconds}s - {raise_msg}')
        return False

    def scroll_to_view(self) -> None:
        elem = self.get_element_object()
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)
        logging.info(f"✅ scroll to elem {elem}")

    def set_border(self, px: int = 2) -> None:
        elem = self.get_element_object()
        try:
            style_red = f'arguments[0].style.border="{px}px solid #FF0000"'
            style_null = 'arguments[0].style.border=""'
            if px:
                self.driver.execute_script(style_red, elem)
            else:
                self.driver.execute_script(style_null, elem)
        except BaseException:
            pass

    # def is_located(self) -> bool:
    #     try:
    #         self.__get_element(self.k, self.v)
    #         return True
    #     except Exception as e:
    #         # logging.error(e)
    #         return False


