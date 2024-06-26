from Code.Common.Common import delete_proxy
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
# from poium.common import logging
from loguru import logger
import traceback
import unittest
import sys


class unittest_Fixtures(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # logger = logging.logger
        # logger.add("../Logs/{time}.log", format=r'{time: YYYY-MM-DD HH:mm:ss} | {file}-{line} | {level} | {message}', level="TRACE", encoding="utf-8")
        logger.warning("SETUP CLASS ========================================")
        logger.info(f"Delete Proxy result is {delete_proxy()}")

        try:
            logger.info("Start to download webDriver.exe")
            driver_path = ChromeDriverManager(path=r"../Drivers").install()
        except BaseException:
            logger.info("Failed download webDriver and start to get it from config")
            driver_path = "Read config"
        logger.success(f"Got it from {driver_path}")
        cls.driver_path = driver_path

        options = ChromeOptions()
        # 忽略提醒，自动化提醒和无用日志
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        # 忽略提醒，证书错误
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        cls.options = options

        try:
            logger.info("Start to test lunch browser")
            driver = Chrome(service=Service(driver_path), options=options)
            driver.quit()
            logger.success("Success lunched")
        except BaseException:
            logger.error(traceback.format_exc())
            logger.error("Please check the webDriver as it failed in lunching browser!")
            logger.error("THE END")
            input("")
            sys.exit()

    @classmethod
    def tearDownClass(cls) -> None:
        logger.warning("TEAR DOWN CLASS ========================================")

    def setUp(self) -> None:
        self.driver = Chrome(service=Service(self.driver_path), options=self.options)
        self.driver.maximize_window()
        logger.info("Lunched Browser")
        logger.warning("START TESTCASE ====================")

    def tearDown(self) -> None:
        logger.warning("E N D TESTCASE ====================")
        if self.driver:
            self.driver.quit()
            logger.info("Quited Browser")

