from common.android_ui_driver import *


class FL_Page(AndroidBasePage):
    random_no_tab = {ElmWith.text: '随机数生成'}
    min_random_input = {ElmWith.text: '最小值..'}
    max_random_input = {ElmWith.text: '最大值..'}
    gen_btn = {ElmWith.business_describe: '生成按钮',
               ElmWith.text: '生成'}

    def test_random_number_tab(self):
        self.loger.info('test_random_number_tab')
        self.android.swipe_down_to_find(**self.random_no_tab).click()
        self.android(**self.min_random_input).set_text('20')
        self.android(**self.max_random_input).set_text('200')
        # self.android.xpath('//android.widget.EditText[@hint="生成数量"]').set_text('')  # xpathSelector没有清空输入框方法
        self.android(**self.gen_btn).click()
        self.android.screenshot()
        pass
