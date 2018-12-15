"""
目标 ;  一个步骤一个方法

"""

import page
from base.base import Base


class PageAoLai(Base):
    # 点击 我  按钮
    def page_me(self):
        self.base_click(page.loc_me)

    # 点击  已有账户,去登录
    def page_name(self):
        self.base_click(page.loc_name)

    # 输入用户名
    def page_username(self, user):
        self.base_send(page.loc_username, user)

    # 输入密码
    def page_password(self, pwd):
        self.base_send(page.loc_password, pwd)

    # 点击登录
    def page_enter(self):
        self.base_click(page.loc_enter)
