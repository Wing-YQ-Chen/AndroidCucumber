import uiautomator2
import logging
from uiautomator2.exceptions import UiObjectNotFoundError
from typing import List

"""
ElmWith 类，定义了一系列与元素相关的属性名称
"""


class ElmWith(object):
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


"""
AndroidElement 类继承自 uiautomator2.UiObject
用于对 Android 页面元素的交互
"""


class AndroidElement(uiautomator2.UiObject):
    """
    初始化方法

    参数：
    session (AndroidDevice)：会话对象
    selector (uiautomator2.Selector)：选择器
    loger (logging.Logger)：日志记录器
    business_describe (str)：业务描述
    """

    def __init__(self, session: 'AndroidDevice',
                 selector: uiautomator2.Selector,
                 loger: logging.Logger,
                 business_describe: str = None,
                 **kwargs):
        super().__init__(session, selector)
        self.kwargs = kwargs
        self._loger = loger
        self.business_describe = business_describe
        self.elm_describe = "<{}>[{}]".format(business_describe if business_describe else self.selector,
                                              kwargs.get('index') if kwargs.get('index') else 1)

    """
    点击元素的方法，并记录日志

    参数：
    timeout (Optional[float])：超时时间，可选
    offset (Optional)：偏移量，可选
    """

    def click(self, timeout=None, offset=None):
        self._loger.info(f'🖱️ Click {self.elm_describe}')
        super().click(timeout, offset)


    """
    尝试点击元素的方法，如果失败则忽略异常

    参数：
    timeout (Optional[float])：超时时间，可选
    offset (Optional)：偏移量，可选
    """

    def try_click(self, timeout=None, offset=None):
        self._loger.info(f'🖱️ Try to click {self.elm_describe}')
        try:
            super().click(timeout, offset)
        except BaseException:
            pass

    """
    等待元素的方法，并记录日志

    参数：
    exists (bool)：元素是否存在
    timeout (Optional[float])：超时时间，可选

    返回：
    bool：元素是否存在
    """

    def waiting(self, exists=True, timeout=None) -> bool:
        self._loger.info(f'⏳ Waiting {timeout if timeout else self.wait_timeout}s for {self.elm_describe}')
        elm_exist = super().wait(exists, timeout)
        if elm_exist != exists:
            self._loger.info('❌ Element is {} for {}'.format(
                'not existing' if exists else 'existing', self.elm_describe))
        return elm_exist

    """
    为元素设置文本的方法，并记录日志

    参数：
    text (str)：要设置的文本
    timeout (Optional[float])：超时时间，可选
    """

    def set_text(self, text, timeout=None):
        self._loger.info(f'🎹 Input {text} to {self.elm_describe}')
        super().set_text(text, timeout)

    """
    获取多个元素, 注意这个搜索是没有任何隐式等待的

    返回：
    is_list (List['IosSelector'])：IosSelector 元素列表
    """

    def gets(self) -> List['AndroidElement']:
        # self.kwargs.pop('index')
        is_list = []
        ec = self.count
        for i in range(1, ec + 1):
            is_list.append(AndroidElement(self.session, uiautomator2.Selector(**self.kwargs), self._loger, self.business_describe))
        self._loger.info(f'🎨 Got {ec} elements for {self.business_describe}')
        return is_list

    """
    强制等待元素的方法，如果未找到则抛出异常

    参数：
    exists (bool)：元素是否存在
    timeout (Optional[float])：超时时间，可选
    """

    def must_wait(self, exists=True, timeout=None):
        if not self.wait(exists, timeout):
            raise UiObjectNotFoundError(f'⛔ Element not found for {self.elm_describe}')
