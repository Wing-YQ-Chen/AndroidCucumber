import logging
from .IosDevice import IosDevice


class IosBasePage(object):

    def __init__(self, ios: IosDevice, loger: logging.Logger = logging.getLogger()):
        self.ios = ios
        self._loger = loger
