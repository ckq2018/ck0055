"""

目标 : 封装点击方法和输入方法
"""


from selenium.webdriver.support.wait import WebDriverWait


class Base():
    #初始化driver
    def __init__(self, driver):
        self.driver = driver


    # 先获取元素     采用二次封装  使用显示等待
    def base_find(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        self.base_find(loc).click()

    # 输入方法
    def base_send(self, loc, value):
        # 先获取元素
        el = self.base_find(loc)
        # 首先清空文本框,有些文本框会有默认值
        el.clear()
        # 输入内容  内容不能固定
        el.send_keys(value)
