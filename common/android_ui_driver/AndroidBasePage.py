import logging
from .AndroidDevice import AndroidDevice


class AndroidBasePage(object):

    def __init__(self, android: AndroidDevice, loger: logging.Logger = logging.getLogger()):
        self.android = android
        self._loger = loger
