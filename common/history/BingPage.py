from poium import *
"""
Pages API is use for Browser
Element API is use for Element 
"""


class BingPage(Page):
    """baidu page"""
    search_input = Element(id_="sb_form_q", describe="输入框")
    search_button = Element(id_="search_icon", describe="搜索按钮")
