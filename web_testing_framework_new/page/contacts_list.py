from selenium.webdriver.common.by import By

from web_testing_framework_new.base.base import Base


class ContactsListPage(Base):
    """
    成员列表页面
    https://work.weixin.qq.com/wework_admin/frame#contacts
    """

    _init_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    """初始化时的url"""

    __member_list_phone = (By.XPATH, '//*[@id="member_list"]/tr/td[5]')
    """列表里的手机号"""

    def get_phone_list(self) -> list:
        """
        获取成员列表的手机号
        return: 成员的手机号
        """
        return self.get_text_list(self.__member_list_phone)
