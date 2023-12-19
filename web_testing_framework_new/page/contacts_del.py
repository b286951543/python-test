from selenium.webdriver.common.by import By

from web_testing_framework_new.base.base import Base
from web_testing_framework_new.page.contacts_list import ContactsListPage


class ContactsDelPage(Base):
    """
    删除成员页面
    https://work.weixin.qq.com/wework_admin/frame#contacts
    """

    __del_btn = (By.CSS_SELECTOR, '.member_colRight_operationBar.ww_operationBar > .js_del_member')
    """删除按钮"""

    __dialog_del_btn = (By.CSS_SELECTOR, '.ww_dialog_foot > .ww_btn_Blue')
    """弹窗的删除按钮"""

    # 如果在这个页面实例化, 会修改 Base 里 _init_url 变量的值
    _init_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    """初始化时的url"""

    def contacts_del(self, ele) -> ContactsListPage:
        """
        删除成员操作
        return: 成员列表页面
        """

        # 删除
        self.driver.find_element(*self.__del_btn).click()
        self.driver.find_element(*self.__dialog_del_btn).click()
        # 返回成员列表页面
        return ContactsListPage(self.driver)
