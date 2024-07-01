import time
from behave import *
from common.android_ui_driver import AndroidDevice, ElmWith
from behave.__main__ import main as behave_main

product = {ElmWith.className: 'android.view.ViewGroup',
           ElmWith.index: 2}
lunched_elm = {ElmWith.business_describe: '启动成功标志',
               ElmWith.text: 'WoodBox'}
allow_lunch_app_btn = {ElmWith.business_describe: '允许启动淘宝',
                       ElmWith.className: 'android.widget.Button',
                       ElmWith.resourceId: 'android:id/button1'}


@given('user is on the home page of SAK app')
def lunch_app(context):
    context.ad = AndroidDevice('ba151d69')
    context.ad.app_stop('com.taobao.taobao')
    context.ad.app_start(package_name='com.One.WoodenLetter', wait=True, stop=True)
    time.sleep(1)
    context.ad(**lunched_elm).click()

    # ad(text='Tb Coupon Query').click()
    # assert ad(text='精选优品').waiting()
    # ad(**product).click()
    # ad(**allow_lunch_app_btn).try_click(5)
    # assert ad(text='粉丝福利购').waiting()
    # ad(text='立即领券').click()
    # assert ad(text='领券购买').waiting()
    # ad.screenshot('test.png')


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
    assert context.ad(text='领券购买').waiting()


if __name__ == '__main__':
    pass
    behave_main()
    # lunch_app(None)
