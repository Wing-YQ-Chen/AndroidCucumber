import os
import re

from func_timeout import func_set_timeout
from common.utils import get_timestamp_str
from poium import Page as poium_Page
from loguru import logger
from selenium.webdriver.remote.webdriver import WebDriver


class WebBasicPage(poium_Page):
    driver: WebDriver

    def close_windows(self, except_re_list: [str] = []):
        temp = self.driver.window_handles
        self.window_scroll()
        for handle in temp:
            try:
                self.driver.switch_to.window(handle)
            except BaseException:
                logger.info(f"This window not existing already '{handle}'")
                continue
            title = self.driver.title
            logger.debug(f"title is '{title}'")
            for re_str in except_re_list:
                if re.findall(re_str, title):
                    break
            else:
                logger.info(f"Closing window '{title}'")
                self.driver.close()

    def refresh_page(self):
        self.driver.refresh()

    def switch_frame(self, frame_reference=None):
        if frame_reference:
            self.driver.switch_to.frame(frame_reference)
        else:
            self.driver.switch_to.default_content()

    def screenshotting(self, save_dir_path=".", file_name: str = "", full_flag: bool = False,
                       height_multiplier: float = 1, width_multiplier: float = 1):
        if not save_dir_path:
            return ""
        try:
            return self.__screenshot(save_dir_path, file_name, full_flag, height_multiplier, width_multiplier)
        except BaseException:
            return "Fail to take screenshot"

    @func_set_timeout(30)
    def __screenshot(self, save_dir_path, file_name, full_flag, height_multiplier, width_multiplier):
        current_width = self.driver.get_window_size()['width']
        current_height = self.driver.get_window_size()['height']
        if full_flag:
            body_width = self.driver.execute_script("return document.body.scrollWidth")
            body_height = self.driver.execute_script("return document.body.scrollHeight")
            self.driver.set_window_size(body_width * width_multiplier, body_height * height_multiplier)
            self.sleep(1)
        save_dir_path = os.path.abspath(save_dir_path)
        if not os.path.exists(save_dir_path):
            os.makedirs(save_dir_path)
        save_path = os.path.join(save_dir_path, f'{file_name}.png')
        if os.path.exists(save_path):
            save_path = os.path.join(save_dir_path, f'{file_name}-{get_timestamp_str()}.png')
        self.driver.save_screenshot(save_path)
        if full_flag:
            self.driver.set_window_size(current_width, current_height)
        return save_path
