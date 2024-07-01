import time
import android_device

class AndroidBasePage(object):

    def __init__(self, android: 'android_device.AndroidDevice'):
        self.android = android
        self.loger = android.loger

    def sleep(self, s):
        self.loger.info(f'🌙 Sleeping {s}s')
        time.sleep(s)
