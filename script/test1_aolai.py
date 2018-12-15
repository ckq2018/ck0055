"""
目标 : 不用过脑,三个步骤
"""
# 解决路径问题
import sys
import os

import pytest

sys.path.append(os.getcwd())



from base.get_driver import get_driver
from page.page_aolai import PageAoLai


class TestAoLai():
    # 实例化页面对象
    def setup_class(self):
        self.page = PageAoLai(get_driver())

    # 关闭driver对象
    def teardown_class(self):
        self.page.driver.quit()

    # 参数化
    @pytest.mark.parametrize("user, pwd", [(1383838, 123456)])
    # 测试方法
    def test_aolai(self, user, pwd):
        # 第一步,点击 我
        self.page.page_me()
        # 第二步,点击 已有账户,去登录
        self.page.page_name()
        # 第三步,输入用户名
        self.page.page_username(user)
        # 第四步,输入密码
        self.page.page_password(pwd)
        # 第五步,点击登录
        self.page.page_enter()
