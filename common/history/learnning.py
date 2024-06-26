from Code.PageObject.BingPage import BingPage
from Code.Common.unittest_Fixtures import unittest_Fixtures
import unittest

"""
unitest - 组织脚本运行
poium  - 提高代码开发和维护的效率 
    基于PO设计模式，对以下API进行二次封装的框架
    Selenium.WebDriver
    Appium.WebDriver
"""


class test_class(unittest_Fixtures):

    # data drive
    def test_run(self):
        page = BingPage(self.driver)
        page.open("https://cn.bing.com/")
        page.search_input.send_keys("Selenium")
        page.search_input.send_keys("1", True, True)
        page.search_button.click()

    def test_run2(self):
        page = BingPage(self.driver)
        page.open("https://cn.bing.com/")
        page.search_input.send_keys("Python")
        page.search_input.send_keys("2", True, True)
        page.search_button.click()

    def test_run3(self):
        page = BingPage(self.driver)
        page.open("https://cn.bing.com/")
        page.search_input.send_keys("哈哈哈")
        page.search_input.send_keys("3", True, True)
        page.search_button.click()


if __name__ == '__main__':
    unittest.main()
