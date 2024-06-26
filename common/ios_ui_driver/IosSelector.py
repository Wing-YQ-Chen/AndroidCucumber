import wda
import logging
import time
from wda.exceptions import *
from wda import Element
from wda import Rect


class ElmWith(object):
    business_describe = 'business_describe'
    predicate = 'predicate'
    id = 'id'
    className = 'className'
    type = 'type'
    name = 'name'
    nameContains = 'nameContains'
    nameMatches = 'nameMatches'
    text = 'text'
    textContains = 'textContains'
    textMatches = 'textMatches'
    value = 'value'
    valueContains = 'valueContains'
    label = 'label'
    labelContains = 'labelContains'
    visible = 'visible'
    enabled = 'enabled'
    classChain = 'classChain'
    xpath = 'xpath'
    parent_class_chains = 'parent_class_chains'
    timeout = 'timeout'
    index = 'index'


class IosSelector(wda.Selector):

    def __init__(self,
                 session: wda.Client,
                 loger: logging.Logger,
                 business_describe: str = None,
                 **kwargs):
        wda.Selector.__init__(self, session, **kwargs)

        self.session = session
        self._loger = loger
        self.business_describe = f'<{business_describe if business_describe else self._gen_class_chain()}>'
        self.kwargs = kwargs

    def find_elements(self):
        """
        Returns:
            Element (list): all the elements
        """
        es = []
        for element_id in self.find_element_ids():
            e = Element(self._session, element_id)
            es.append(e)
        return es

    def get(self, timeout=None, raise_err_not_found=True, raise_err_not_displayed=True) -> 'Element':
        """
        Args:
            timeout (float): timeout for query element, unit seconds
                Default 10s
            raise_err_not_found (bool): whether to raise error if element not found
            raise_err_not_displayed (bool): whether to raise error if element found but not displayed

        Returns:
            Element: UI Element

        Raises:
            WDAElementNotFoundError if raise_error is True else None
        """
        start_time = time.time()
        if timeout is None:
            timeout = self._timeout
        while True:
            elm_ids = self.find_element_ids()
            if elm_ids:
                elm = Element(self.session, elm_ids[0])
                if not elm.displayed:
                    e_msg = f'⚠️ Element found. But it not displayed for {self.business_describe}'
                    self._loger.warning(e_msg)
                    if raise_err_not_displayed:
                        raise WDAElementNotFoundError(e_msg)
                return elm
            if start_time + timeout < time.time():
                e_msg = f'⛔ Element not found for {self.business_describe}'
                self._loger.warning(e_msg)
                if raise_err_not_found:
                    raise WDAElementNotFoundError(e_msg)
                return None
            time.sleep(0.5)

    def click(self, timeout=None):
        self._loger.info(f'🖱️ Click {self.business_describe}')
        self.get(timeout=timeout).click()

    def try_click(self, timeout=None):
        try:
            self.click(timeout)
        except BaseException:
            pass

    def set_text(self, value, timeout=None):
        self._loger.info(f'🎹 Input {value} to {self.business_describe}')
        self.get(timeout).set_text(value)

    def wait(self, timeout=None, raise_error=False):
        self._loger.info(f'⏰ Waiting {timeout if timeout else self._timeout}s for {self.business_describe}')
        return self.get(timeout, raise_error, raise_error)

    @property
    def info(self):
        return self.get(raise_err_not_displayed=False).info

    @property
    def id(self):
        return self.get(raise_err_not_displayed=False).id

    @property
    def label(self):
        return self.get(raise_err_not_displayed=False).label

    @property
    def className(self):
        return self.get(raise_err_not_displayed=False).className

    @property
    def text(self):
        return self.get(raise_err_not_displayed=False).text

    @property
    def name(self):
        return self.get(raise_err_not_displayed=False).name

    @property
    def displayed(self):
        return self.get(raise_err_not_displayed=False).displayed

    @property
    def enabled(self):
        return self.get(raise_err_not_displayed=False).enabled

    @property
    def accessible(self):
        return self.get(raise_err_not_displayed=False).accessible

    @property
    def accessibility_container(self):
        return self.get(raise_err_not_displayed=False).accessibility_container

    @property
    def value(self):
        return self.get(raise_err_not_displayed=False).value

    @property
    def visible(self):
        return self.get(raise_err_not_displayed=False).visible

    @property
    def bounds(self) -> Rect:
        return self.get(raise_err_not_displayed=False).bounds
