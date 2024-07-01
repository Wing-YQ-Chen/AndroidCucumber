from .AndroidDevice import *
import time


class AndroidBasePage(object):

    def __init__(self, android: 'AndroidDevice'):
        self.android = android
        self.loger = android.loger

    def sleep(self, s):
        self.loger.info(f'🌙 Sleeping {s}s')
        time.sleep(s)
