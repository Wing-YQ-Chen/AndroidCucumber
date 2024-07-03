import time
from .AndroidDevice import AndroidDevice

"""
AndroidBasePage 类，作为 Android 相关页面的基类
"""


class AndroidBasePage(object):
    """
    初始化方法

    参数：
    android (AndroidDevice)：Android 设备对象
    """

    def __init__(self, android: 'AndroidDevice'):
        self.android = android
        self.loger = android.loger

    """
    睡眠方法，用于暂停指定的秒数，并记录日志

    参数：
    s (float)：要暂停的秒数
    """

    def sleep(self, s):
        self.loger.info(f'🌙 Sleeping {s}s')
        time.sleep(s)
