import uiautomator2
import adbutils
import logging
from .AndroidElement import AndroidElement
from typing import Optional, Union


class AndroidDevice(uiautomator2.Device):
    """
    AndroidDevice 是所有 Android 设备类的基类。
    """

    def __init__(self, serial: Union[str, adbutils.AdbDevice] = None, loger: logging.Logger = logging.getLogger()):
        """
        初始化 AndroidDevice 类。

        :param serial: Android设备的序列号或ADB设备实例
        :param loger: 日志记录器
        """
        if not serial:
            serial = adbutils.adb.device()
        self.loger = loger
        self.loger.info(f'📱 Connecting Android Device {serial}')
        uiautomator2.Device.__init__(self, serial)
        self.implicitly_wait(10)

    def connect(self, serial: Union[str, adbutils.AdbDevice] = None) -> 'AndroidDevice':
        """
        重新连接 AndroidDevice。

        :param serial: Android设备的序列号或ADB设备实例
        :return: AndroidDevice 实例
        """
        self.loger.info(f'📱 Reconnecting Android Device {serial}')
        super().__init__(serial)
        return self

    def app_start(self, package_name: str, activity: Optional[str] = None, wait: bool = False, stop: bool = False,
                  use_monkey: bool = False):
        """
        启动 Android 应用程序。

        :param package_name: 应用程序的包名
        :param activity: 应用程序的入口Activity
        :param wait: 是否等待应用程序启动完成
        :param stop: 是否在启动应用程序前停止当前运行的应用程序
        :param use_monkey: 是否使用 monkey 命令启动应用程序
        """
        self.loger.info(f'🍎 App start {package_name}')
        super().app_start(package_name, activity, wait, stop, use_monkey)

    def swipe_down(self):
        """
        向下滑动设备屏幕。
        """
        self.loger.info(f'👇 Swipe down')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    def swipe_up(self):
        """
        向上滑动设备屏幕。
        """
        self.loger.info(f'👆 Swipe Up')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    def swipe(self, fx, fy, tx, ty, duration: Optional[float] = None, steps: Optional[int] = None):
        """
        在设备屏幕上滑动。

        :param fx: 滑动开始时的 x 坐标
        :param fy: 滑动开始时的 y 坐标
        :param tx: 滑动结束时的 x 坐标
        :param ty: 滑动结束时的 y 坐标
        :param duration: 滑动持续时间，单位为秒
        :param steps: 滑动步数，与 duration 至少有一个参数需要提供
        """
        self.loger.info(f'⭐ Swipe [{fx, fy}] -> [{tx, ty}]')
        super().swipe(fx, fy, tx, ty, duration, steps)

    def swip_down_to_find(self, times: int = 10, business_describe: str = None, **kwargs) -> 'AndroidElement' or None:
        """
        向下滑动设备屏幕，查找指定的元素。

        :param times: 滑动次数
        :param business_describe: 业务描述
        :param kwargs: 选择器的参数
        :return: 找到的元素，如果未找到则返回 None
        """
        for i in range(times):
            elm = self.__call__(business_describe, **kwargs)
            if elm.waiting(timeout=1):
                return elm
            self.swipe_down()
        return None

    def __call__(self, business_describe: str = None, **kwargs) -> 'AndroidElement':
        """
        调用 AndroidDevice 实例，返回一个 AndroidElement 对象。

        :param business_describe: 业务描述
        :param kwargs: 选择器的参数
        :return: AndroidElement 对象
        """
        return AndroidElement(self, uiautomator2.Selector(**kwargs), self.loger, business_describe)
