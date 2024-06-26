from Code.PageObject.NBS_Pages import NBS_Home_Page, DC_Page
from Code.Common.unittest_Fixtures import unittest_Fixtures
from ddt import ddt, data
from loguru import logger

from Code.Common.Common import *
import traceback
import unittest
import glob
import os.path
import openpyxl

logger.add("../Logs/{time}.log", format=r'{time: YYYY-MM-DD HH:mm:ss} | {file}-{line} | {level} | {message}', level="DEBUG", encoding="utf-8")


def get_input_data():
    logger.info('Finding the input file')
    temp_var = os.path.abspath('../Input/*.xlsx')
    input_file_path = glob.glob(temp_var)
    if input_file_path:
        pass
    else:
        msg = f'Failed Extracting input data.'
        logger.error(msg)
        raise FileNotFoundError(msg)

    xl_table = None
    try:
        logger.info('Extracting input data')
        xl_table = [  # get table of input data from excel
            ['1', '42370388', 'HVY1'],
            ['2', '42370389', 'HVY2']
        ]
    except BaseException as e:
        logger.error(f'Failed Extracting input data.\n{traceback.format_exc()}')
        raise e

    return xl_table


@ddt
class NBS_UI_capture(unittest_Fixtures):

    @data(*get_input_data())
    def test_run(self, case_datas):
        case_number = case_datas[0]
        policy = case_datas[1]
        product_code = case_datas[2]
        logger.info(f'executing: {case_number} {policy} {product_code}')

        try:
            NBSU201_link = r"https://hkgnbsappuat07.hk.intranet:8443/dsia/logoff.do"
            NBS_Home_page = NBS_Home_Page(self.driver)
            NBS_Home_page.login(NBSU201_link, "utnbsh", "Today@NBD")
            NBS_Home_page.enter_modification_page()

            DC_page = DC_Page(self.driver)
            DC_page.capture(policy)  # return a dict result
            # create_report_xl()
            # create a result Excel file with template file. and with key mapping on sheet
            # record dict result on sheet by key mapping. and ignore the result key which the sheet key dose not has.
        except BaseException:
            logger.error(f'Occurred an unknow error during test case running.\n{traceback.format_exc()}')

        pass


if __name__ == '__main__':
    unittest.main()

    """
    get data
    setup class
    setup
    down
    down class
    """

    """
    unitest - 组织脚本运行
    poium  - 提高代码开发和维护的效率
        基于PO设计模式，对以下API进行二次封装的框架
        Selenium.WebDriver
        Appium.WebDriver
    """
