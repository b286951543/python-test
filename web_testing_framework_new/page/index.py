from selenium.webdriver.common.by import By

from web_testing_framework_new.base.base import Base
from web_testing_framework_new.page.contacts_add import ContactsAddPage
from web_testing_framework_new.page.contacts_list import ContactsListPage


class IndexPage(Base):
    """
    首页
    https://work.weixin.qq.com/wework_admin/frame#index
    """

    __member_add_btn = (By.XPATH, '//span[text()="添加成员"]')
    """添加成员的按钮"""

    __member_list_btn = (By.XPATH, '//*[@id="menu_contacts"]')
    """通讯录的按钮"""

    _init_url = 'https://work.weixin.qq.com/wework_admin/frame#index'
    """初始化时的url"""

    def goto_contacts_add(self) -> ContactsAddPage:
        """
        进入添加成员页面
        return: 添加成员页面
        """

        # 这里主要要使用 * 号用于迭代元组的内容
        self.click(self.__member_add_btn)
        # 返回添加成员页面
        return ContactsAddPage(self.driver)

    def goto_contacts_list(self) -> ContactsListPage:
        """
        进入通讯录页面
        return: 通讯录页面
        """

        # 这里主要要使用 * 号用于迭代元组的内容
        self.click(self.__member_add_btn)
        # 返回添加成员页面
        return ContactsAddPage(self.driver)