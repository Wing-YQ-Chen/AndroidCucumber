from common.log import setup_logging
from common.android_ui_driver import AndroidDevice
from SAK_scripts.Pages.FL_Page import FL_Page

if __name__ == '__main__':
    ad = AndroidDevice('ba151d69', setup_logging())
    ad.app_start(package_name='com.One.WoodenLetter', wait=True, stop=True)
    cp = FL_Page(ad)
    cp.test_random_number_tab()
    ad.screenshot()
