from Code.Common.Common import delete_proxy
from Code.Common.Common import setup_logger
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from poium.common import logging
# from loguru import logger
import pytest
import traceback

# logger = setup_logger("../Logs")
logger = logging.logger


@pytest.fixture(scope="session")
def get_webdriver_path():
    """
    Try to download WebDriver
    :return: A WebDriver path
    """
    logger.add("../Logs/{time}.log", format=r'{time: YYYY-MM-DD HH:mm:ss} | {file}-{line} | {level} | {message}',
               level="TRACE",encoding="utf-8")
    # logging.logger = logger
    logger.info(f"Delete Proxy result is {delete_proxy()}")
    try:
        logger.info("Start to download WebDriver")
        driver_path = ChromeDriverManager(path=r"../Drivers").install()
        logger.info("Download is success")
    except BaseException:
        logger.error(traceback.format_exc())
        logger.error("Download is Failed and Start to get config")
        driver_path = "Config"
    logger.info(driver_path)
    yield driver_path


@pytest.fixture(scope="function", name="webdriver")
def setup_webdriver(get_webdriver_path):
    logger.info(f"Launching Browser")
    try:
        driver = Chrome(service=Service(get_webdriver_path))
    except BaseException as e:
        logger.error(traceback.format_exc())
        logger.error("Failed in Launching Browser")
        raise e
    logger.warning("====================START FUNCTION====================")
    yield driver
    logger.warning("====================E N D FUNCTION====================")
    if driver: driver.quit()
    logger.info("Closed Browser")
