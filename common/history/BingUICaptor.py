from Code.PageObject.BingPage import BingPage
from Code.Common.unittest_Fixtures import unittest_Fixtures
from loguru import logger

from Code.Common.Common import *
import traceback
import unittest
import glob
import os.path
import openpyxl
import sys


class BingUICaptor(object):

    def __init__(self):
        logger.info('Initialling the Captor')
        # self.driver_path, self.options = setup_webdriver()
        self.driver = None
        self.result = None
        self.screenshot_path = None
        report_name = r"NBS_script UI capture report"
        report_dir_path = os.path.abspath('../Report')
        # self.report_path = create_report_xl(report_template_path, report_dir_path, report_name, [0, 1])

    def lunch_browser(self):
        logger.info('Lunching the Browser')
        # self.driver = webdriver.Chrome(service=Service(self.driver_path), options=self.options)
        options = ChromeOptions()
        # 忽略提醒，自动化提醒和无用日志
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        # 忽略提醒，证书错误
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        options.add_argument("–disable-notifications")
        options.add_argument("lang=en_US")
        chrome = {
            "browserName": "chrome"
        }
        self.driver = webdriver.Remote("http://localhost:4444/wd/hub", desired_capabilities=chrome, options=options)
        # self.driver = webdriver.Remote("http://127.0.0.1:2375/wd/hub", desired_capabilities=chrome, options=options)
        self.driver.maximize_window()

    def execute(self, case_number, policy_number, link, username, password):
        self.result = None
        self.screenshot_path = None
        Bing_page = BingPage(self.driver)
        try:
            Bing_page.open(link)
            Bing_page.search_input.input(f"Docker learning {case_number} {policy_number}")
            Bing_page.search_button.click()
            self.result = Bing_page.result_list.get_attribute('textContent')
            logger.info(f'This case execution successfully "{case_number}" "{policy_number}"')
        except BaseException:
            logger.error(f'This case occurred an exception error as below during executing '
                         f'”{case_number}" "{policy_number}"\n{traceback.format_exc()}')
            self.screenshot_path = "screen test"
            # Bing_page.screenshots()

    def quit_browser(self):
        if self.driver:
            logger.info('Quiting Browser')
            self.driver.quit()

    def record_result(self):
        # 记录报告, 匹配表头字段地写入
        try:
            logger.info(f'Recorded result\n{self.result}')
        except BaseException:
            logger.error(f'occurred an exception error during record to report')


def main():
    username = os.getlogin()
    logger.add("../Logs/" + username + " {time}.log",
               format=r'{time:YYYY-MM-DD HH:mm:ss} | {file}-{line} | {level} | {message}',
               level="DEBUG", encoding="utf-8")
    logger.info(f"{username} running {os.path.basename(sys.argv[0])}")

    logger.info('Finding the input file.')
    input_file_search_str = os.path.abspath('../Input/*.xlsx')
    input_file_path = glob.glob(input_file_search_str)
    if input_file_path:
        input_file_path = input_file_path[0]
        logger.info(f'Got the input file from below path\n{input_file_path}')

        input_wk = openpyxl.load_workbook(input_file_path, True)
        input_ws = input_wk.worksheets[0]
        input_cases = input_ws["A7":"C" + input_ws.max_row.__str__()]
        nbs_link = input_ws['B3'].value.__str__().strip()
        username = input_ws['B4'].value.__str__().strip()
        password = input_ws['B5'].value.__str__().strip()
        input_wk.close()

        if input_cases:
            captor = BingUICaptor()
            for i in range(input_cases.__len__()):
                case_number = input_cases[i][0].value.__str__().strip()
                policy_number = input_cases[i][1].value.__str__().strip()
                logger.info(f'Executing "{case_number}" "{policy_number}"')
                captor.lunch_browser()
                captor.execute(case_number, policy_number, nbs_link, username, password)
                # captor.quit_browser()
                captor.record_result()
                logger.info('Next')
            logger.info('All cases execution done')

        else:
            logger.warning('Input file is blank. Please check.')
            input('END')
    else:
        logger.warning(f'Not found the input file from below path\n{input_file_search_str}')
        input('END')


if __name__ == '__main__':
    main()
    """
    程序开始
        建立日志
        搜索输入文件
        成功发现
            记录日志
            读取输入文件
            创建报告文件
            实例执行对象
            遍历输入数据
                记录日志
                执行启动浏览
                执行获取页面文本
                执行退出浏览器
                写入并保存报告
                记录日志
                下一个
            记录日志
        否则
            记录日志
    程序结束
    
docker run --rm --name selenium-docker -p 4444:4444 `
-v ${PWD}/config.toml:/opt/bin/config.toml `
-v ${PWD}/assets:/opt/selenium/assets `
-v /var/run/docker.sock:/var/run/docker.sock `
selenium/standalone-docker
    """
