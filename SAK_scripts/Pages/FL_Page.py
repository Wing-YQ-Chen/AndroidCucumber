from common.android_ui_driver import *
from common.log import setup_logging


class FL_Page(AndroidBasePage):
    random_no_tab = {ElmWith.text: '随机数生成'}
    min_random_input = {ElmWith.text: '最小值..'}
    max_random_input = {ElmWith.text: '最大值..'}
    gen_counts = {ElmWith.business_describe: '生成数量',
                  ElmWith.resourceId: 'com.One.WoodenLetter:id/bin',
                  ElmWith.text: '生成数量',
                  ElmWith.className: 'android.widget.EditText'}

    def test_random_number_tab(self):
        self.loger.info('test_random_number_tab')
        # self.android.swipe_down_to_find(**self.random_no_tab).click()
        self.android(**self.min_random_input).set_text('1')
        self.android(**self.max_random_input).set_text('100')
        # self.android.xpath('//android.widget.EditText[@hint="生成数量"]').set_text('')  # xpathSelector没有清空输入框方法
        self.android(**self.gen_counts).set_text('15')
        pass


if __name__ == '__main__':
    ad = AndroidDevice('ba151d69', setup_logging())
    # ad.app_start(package_name='com.One.WoodenLetter', wait=True, stop=True)
    cp = FL_Page(ad)
    cp.test_random_number_tab()
