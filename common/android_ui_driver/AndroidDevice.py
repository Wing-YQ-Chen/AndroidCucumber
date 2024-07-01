import uiautomator2
import adbutils
import logging
from typing import Optional, Union
from .AndroidElement import AndroidElement


class AndroidDevice(uiautomator2.Device):

    def __init__(self, serial: Union[str, adbutils.AdbDevice] = None, loger: logging.Logger = logging.getLogger()):
        if not serial:
            serial = adbutils.adb.device()
        self.loger = loger
        self.loger.info(f'📱 Connecting Android Device {serial}')
        uiautomator2.Device.__init__(self, serial)
        self.implicitly_wait(10)

    def connect(self, serial: Union[str, adbutils.AdbDevice] = None) -> 'AndroidDevice':
        self.loger.info(f'📱 Reconnecting Android Device {serial}')
        super().__init__(serial)
        return self

    def app_start(self, package_name: str, activity: Optional[str] = None, wait: bool = False, stop: bool = False,
                  use_monkey: bool = False):
        self.loger.info(f'🍎 App start {package_name}')
        super().app_start(package_name, activity, wait, stop, use_monkey)

    def swipe_down(self):
        self.loger.info(f'👇 Swipe down')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    def swipe_up(self):
        self.loger.info(f'👆 Swipe Up')
        super().swipe(0.5, 0.8, 0.5, 0.2, steps=180)

    def swipe(self, fx, fy, tx, ty, duration: Optional[float] = None, steps: Optional[int] = None):
        self.loger.info(f'⭐ Swipe [{fx, fy}] -> [{tx, ty}]')
        super().swipe(fx, fy, tx, ty, duration, steps)

    def swip_down_to_find(self, times: int = 10, business_describe: str = None, **kwargs) -> 'AndroidElement' or None:
        for i in range(times):
            elm = self.__call__(business_describe, **kwargs)
            if elm.waiting(timeout=1):
                return elm
            self.swipe_down()
        return None

    def __call__(self, business_describe: str = None, **kwargs) -> 'AndroidElement':
        return AndroidElement(self, uiautomator2.Selector(**kwargs), self.loger, business_describe)
