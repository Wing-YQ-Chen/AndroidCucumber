from android_ui_driver import *


class AD_page(object):
    a_button_elm = {ElmWith.text: 'submit', ElmWith.business_describe: 'submit policy'}

    def __init__(self, ad: AndroidDriver):
        self.ad = ad
        self.ad(**self.a_button_elm).click()
        self.ad(**self.a_button_elm).set_text()

    def run_script(self):
        pass


if __name__ == '__main__':
    ad = AndroidDriver('ba151d69', setup_logging())
    ad_page = AD_page(ad)
    ad_page.run_script()
