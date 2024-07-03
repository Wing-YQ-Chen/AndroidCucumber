from common.android_ui_driver import *
from common.log import setup_logging

"""
CategoriesPage 类继承自 AndroidBasePage，用于处理特定的分类页面操作
"""


class CategoriesPage(AndroidBasePage):
    product = {ElmWith.className: 'android.view.ViewGroup',
               ElmWith.index: 2}
    lunched_elm = {ElmWith.business_describe: '启动成功标志',
                   ElmWith.text: 'WoodBox'}
    allow_lunch_app_btn = {ElmWith.business_describe: '允许启动淘宝',
                           ElmWith.className: 'android.widget.Button',
                           ElmWith.resourceId: 'android:id/button1'}

    """
    访问一个标签的方法
    """

    def access_a_tab(self):
        self.loger.info('access_a_tab')
        e = self.android(**self.lunched_elm)
        e.click()
        for e in self.android(**self.lunched_elm).gets():
            e.click()


if __name__ == '__main__':
    ad = AndroidDevice('ba151d69', setup_logging())
    ad.app_start(package_name='com.One.WoodenLetter', wait=True, stop=True)
    cp = CategoriesPage(ad)
    cp.access_a_tab()
