from appium.webdriver.common.appiumby import AppiumBy

from app_testing_framework.base.base import Base
from app_testing_framework.page.member_add import MemberAddPage


class ContactsAddPage(Base):
    """
    添加成员页面
    """

    __member_add_btn = (AppiumBy.XPATH, '//*[@text="手动输入添加"]')
    """手动输入添加 按钮"""

    def goto_member_add(self) -> MemberAddPage:
        """
        进入手动输入添加成员页面
        """
        self.click(*self.__member_add_btn)
        # 手动输入添加成员页面
        return MemberAddPage(self.driver)

    def get_toast_text(self):
        """
        获取弹窗的内容
        """
        text = self.get_toast_text_by_class()
        return text