from selenium.webdriver.common.by import By

from app_testing_framework.base.base import Base
from app_testing_framework.page.contacts_list import ContactsListPage


class IndexPage(Base):
    """
    首页
    """

    __member_add_btn = (By.XPATH, '//span[text()="添加成员"]')
    """添加成员的按钮"""

    __member_list_btn = (By.XPATH, '//*[text()="通讯录"]')
    """通讯录的按钮"""

    def goto_contacts_list(self) -> ContactsListPage:
        """
        进入通讯录页面
        return: 通讯录页面
        """

        self.click(self.__member_list_btn)
        # 返回通讯录页面
        return ContactsListPage(self.driver)