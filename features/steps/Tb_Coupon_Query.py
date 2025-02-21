import time
from behave import *
from common.android_ui_driver import AndroidDevice, ElmWith
from behave.__main__ import main as behave_main

product = {ElmWith.className: 'android.view.ViewGroup',
           ElmWith.index: 2}
taobao_tag = {ElmWith.business_describe: '淘宝页面就绪标志',
              ElmWith.text: '店铺'}
allow_lunch_app_btn = {ElmWith.business_describe: '允许启动淘宝',
                       ElmWith.className: 'android.widget.Button',
                       ElmWith.resourceId: 'android:id/button1'}

@given('user is on the home page of SAK app')
def lunch_app(context):
    context.ad = AndroidDevice()
    context.ad.app_stop('com.taobao.taobao')
    context.ad.app_start(package_name='com.One.WoodenLetter', wait=True, stop=True)
    time.sleep(1)


@when('user click the button of "{button_text}"')
def click_btn_by_text(context, button_text):
    context.ad(text=button_text).click()


@then('user able to see the page of "{elm_text}"')
def check_elm(context, elm_text):
    assert context.ad(text=elm_text).wait()


@when('user click any one product')
def click_any_one_product(context):
    context.ad(**product).click()
    context.ad(**allow_lunch_app_btn).try_click(5)


@then('user able to see the page of product details on Taobao app')
def step_impl(context):
    context.ad.screenshot()
    assert context.ad(**taobao_tag).waiting()


if __name__ == '__main__':
    behave_main()
