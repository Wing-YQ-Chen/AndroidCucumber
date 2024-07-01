import time
from .AndroidDevice import AndroidDevice


class AndroidBasePage(object):
    """
    AndroidBasePage 是所有 Android 页面类的基类。
    """

    def __init__(self, android: 'AndroidDevice'):
        """
        初始化 AndroidBasePage 类。

        :param android: AndroidDevice 实例
        """
        self.android = android
        self.loger = android.loger

    def sleep(self, s):
        """
        使设备等待指定的秒数。

        :param s: 等待的秒数
        """
        self.loger.info(f'🌙 Sleeping {s}s')
        time.sleep(s)

