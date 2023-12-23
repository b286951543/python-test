from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By

from app_testing_framework.base.base import Base
from app_testing_framework.page.contacts_add import ContactsAddPage


class ContactsListPage(Base):
    """
    通讯录页面
    """

    __member_add_btn = (AppiumBy.XPATH, f'//*[@text()="添加成员"]')
    """添加成员按钮"""

    def goto_contacts_add(self) -> ContactsAddPage:
        """
        进入添加成员页面
        return: 添加成员页面
        """

        self.click(*self.__member_add_btn, swipe_switch=True) # 滑动点击
        # self.swipe_find(*self.__member_add_btn).click()
        # 添加成员页面
        return ContactsAddPage(self.driver)


