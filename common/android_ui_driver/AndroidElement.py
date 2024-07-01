import uiautomator2
import logging
from uiautomator2.exceptions import UiObjectNotFoundError


class ElmWith(object):
    """
    属性，用于指定要搜索的元素属性
    """
    text = "text"
    textContains = "textContains"
    textMatches = "textMatches"
    textStartsWith = "textStartsWith"
    className = "className"
    classNameMatches = "classNameMatches"
    description = "description"
    descriptionContains = "descriptionContains"
    descriptionMatches = "descriptionMatches"
    descriptionStartsWith = "descriptionStartsWith"
    checkable = "checkable"
    checked = "checked"
    clickable = "clickable"
    longClickable = "longClickable"
    scrollable = "scrollable"
    enabled = "enabled"
    focusable = "focusable"
    focused = "focused"
    selected = "selected"
    packageName = "packageName"
    packageNameMatches = "packageNameMatches"
    resourceId = "resourceId"
    resourceIdMatches = "resourceIdMatches"
    index = "index"
    instance = "instance"
    business_describe = "business_describe"


class AndroidElement(uiautomator2.UiObject):
    """
    继承自uiautomator2.UiObject类，用于封装UI元素的操作方法
    """

    def __init__(self, session: 'AndroidDevice', selector: uiautomator2.Selector, loger: logging.Logger,
                 business_describe: str = None):
        """
        初始化方法，接收session、selector、loger和business_describe参数
        """
        super().__init__(session, selector)
        self._loger = loger
        self.business_describe = business_describe if business_describe else self.selector

    def click(self, timeout=None, offset=None):
        """
        点击元素的方法，接收timeout和offset参数
        """
        super().click(timeout, offset)
        self._loger.info(f'🖱️ Click {self.business_describe}')

    def try_click(self, timeout=None, offset=None):
        """
        尝试点击元素的方法，接收timeout和offset参数
        """
        try:
            self.click(timeout, offset)
        except BaseException:
            pass

    def waiting(self, exists=True, timeout=None) -> bool:
        """
        等待元素出现或消失的方法，接收exists和timeout参数
        """
        self._loger.info(f'⏰ Waiting {timeout if timeout else self.wait_timeout}s for {self.business_describe}')
        elm_exist = super().wait(exists, timeout)
        if elm_exist != exists:
            self._loger.info('❌ Element is {} for {}'.format(
                'not existing' if exists else 'existing', self.business_describe))
        return elm_exist

    def set_text(self, text, timeout=None):
        """
        设置元素文本的方法，接收text和timeout参数
        """
        self._loger.info(f'🎹 Input {text} to {self.business_describe}')
        super().set_text(text, timeout)

    def must_wait(self, exists=True, timeout=None):
        """
        确保元素存在的方法，接收exists和timeout参数
        """
        if not self.wait(exists, timeout):
            raise UiObjectNotFoundError(f'⛔ Element not found for {self.business_describe}')
