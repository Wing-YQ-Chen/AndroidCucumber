import uiautomator2
import adbutils
import logging
from .AndroidElement import AndroidElement
from typing import Optional, Union

"""
AndroidDevice 类继承自 uiautomator2.Device，用于处理与 Android 设备的交互操作
"""


class AndroidDevice(uiautomator2.Device):
    """
    初始化方法

    参数：
    serial (Union[str, adbutils.AdbDevice])：设备序列号
    loger (logging.Logger)：日志记录器
    """

    def __init__(self, serial: Union[str, adbutils.AdbDevice] = None, loger: logging.Logger = logging.getLogger()):
        if not serial:
            serial = adbutils.adb.device()
        self.loger = loger
        self.loger.info(f'📱 Connecting Android Device {serial}')
        uiautomator2.Device.__init__(self, serial)
        self.implicitly_wait(10)

    """
    重新连接设备的方法

    参数：
    serial (Union[str, adbutils.AdbDevice])：设备序列号

    返回：
    AndroidDevice：自身对象
    """

    def connect(self, serial: Union[str, adbutils.AdbDevice] = None) -> 'AndroidDevice':
        self.loger.info(f'📱 Reconnecting Android Device {serial}')
        super().__init__(serial)
        return self

    """
    启动应用的方法

    参数：
    package_name (str)：应用的包名
    activity (Optional[str])：应用的活动名，可选
    wait (bool)：是否等待，默认为 False
    stop (bool)：是否先停止应用，默认为 False
    use_monkey (bool)：是否使用 Monkey 工具，默认为 False
    """

    def app_start(self, package_name: str, activity: Optional[str] = None, wait: bool = False, stop: bool = False,
                  use_monkey: bool = False):
        self.loger.info(f'🍎 App start {package_name}')
        super().app_start(package_name, activity, wait, stop, use_monkey)

    """
    向下滑动屏幕的方法，并记录日志
    """

    def swipe_down(self):
        self.loger.info(f'👇 Swipe down')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    """
    向上滑动屏幕的方法，并记录日志
    """

    def swipe_up(self):
        self.loger.info(f'👆 Swipe Up')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    """
    自定义滑动屏幕的方法，并记录日志

    参数：
    fx, fy, tx, ty (float)：起始和结束坐标
    duration (Optional[float])：滑动持续时间，可选
    steps (Optional[int])：滑动步数，可选
    """

    def swipe(self, fx, fy, tx, ty, duration: Optional[float] = None, steps: Optional[int] = None):
        self.loger.info(f'⭐ Swipe [{fx, fy}] -> [{tx, ty}]')
        super().swipe(fx, fy, tx, ty, duration, steps)

    """
    向下滑动多次查找元素的方法

    参数：
    times (int)：滑动次数
    business_describe (str)：业务描述
    **kwargs：其他元素选择的关键字参数

    返回：
    AndroidElement 或 None：找到的元素或 None
    """

    def swipe_down_to_find(self, times: int = 10, business_describe: str = None, raise_err_not_found=True, **kwargs) -> 'AndroidElement':
        elm = self(business_describe, **kwargs)
        for i in range(times):
            if elm.waiting(timeout=1, raise_err_not_found=False):
                return elm
            self.swipe_down()
        else:
            if elm.waiting(timeout=1, raise_err_not_found=raise_err_not_found):
                return elm
        return None

    """
    创建 AndroidElement 对象的方法

    参数：
    business_describe (str)：业务描述
    **kwargs：元素选择的关键字参数

    返回：
    AndroidElement：创建的元素对象
    """

    def __call__(self, business_describe: str = None, **kwargs) -> 'AndroidElement':
        return AndroidElement(self, uiautomator2.Selector(**kwargs), self.loger, business_describe, **kwargs)
