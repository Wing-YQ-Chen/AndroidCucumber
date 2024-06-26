import time
import wda
import logging
from .IosSelector import IosSelector


class IosDevice(wda.USBClient):

    def __init__(self, udid: str = "", port: int = 8100, wda_bundle_id=None,
                 loger: logging.Logger = logging.getLogger()):
        self._loger = loger
        self._loger.info(f'📱 Connecting AppStore_script Device {udid}')
        wda.USBClient.__init__(self, udid, port, wda_bundle_id)  # requests==2.28.1
        self.implicitly_wait(10)

    def __call__(self, business_describe: str = None, predicate=None, id=None, className=None, type=None, name=None,
                 nameContains=None, nameMatches=None, text=None, textContains=None, textMatches=None, value=None,
                 valueContains=None, label=None, labelContains=None, visible=None, enabled=None, classChain=None,
                 xpath=None, parent_class_chains=[], timeout=10.0, index=0):
        return IosSelector(self, self._loger, business_describe, predicate=predicate, id=id, className=className,
                           type=type, name=name, nameContains=nameContains, nameMatches=nameMatches, text=text,
                           textContains=textContains, textMatches=textMatches, value=value, valueContains=valueContains,
                           label=label, labelContains=labelContains, visible=visible, enabled=enabled,
                           classChain=classChain, xpath=xpath, parent_class_chains=parent_class_chains, timeout=timeout,
                           index=index)

    def app_launch(self, bundle_id, app_stop=True, arguments=[], environment={}, wait_for_quiescence=False):
        self._loger.info(f'🍎 App start {bundle_id}')
        self.app_stop(bundle_id)
        super().app_launch(bundle_id)

    def swipe_up(self):
        self._loger.info(f'👆 Swipe Up')
        super().swipe_up()  # 原生API的滑动是从中间滑倒边界

    def swipe_down(self):
        self._loger.info(f'👇 Swipe down')
        super().swipe_down()

    def swipe_left(self):
        self._loger.info(f'👈 Swipe left')
        super().swipe_left()

    def swipe_right(self):
        self._loger.info(f'👉 Swipe right')
        super().swipe_right()

    def swipe(self, x1, y1, x2, y2, duration=1):
        self._loger.info(f'⭐ Swipe [{x1, y1}] -> [{x2, y2}]')
        super().swipe(x1, y1, x2, y2, duration)

    def swip_up_to_find(self, times: int = 5,
                        raise_err_not_displayed=True,
                        business_describe: str = None,
                        **kwargs) -> 'IosSelector':
        elm = self.__call__(business_describe, **kwargs)
        for i in range(times):
            elm_found = elm.get(None, False, False)
            if elm_found:
                if raise_err_not_displayed:
                    if elm_found.displayed:
                        return elm
                    else:
                        continue
                else:
                    return elm
            self.swipe_up()
        else:
            if elm.get(None, raise_err_not_displayed, raise_err_not_displayed):
                return elm

    def screenshot(self, png_filename=None, format='pillow'):
        if not png_filename:
            png_filename = '{} AppStore_script.png'.format(time.strftime('%Y%m%d%H%M%S', time.localtime()).__str__())
        self._loger.info(f'📸 Screenshot to {png_filename}')
        super().screenshot(png_filename, format)
