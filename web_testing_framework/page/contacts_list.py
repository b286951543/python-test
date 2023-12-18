from selenium.webdriver.common.by import By

from web_testing_framework.base.base import Base


class ContactsListPage(Base):
    """
    成员列表页面
    https://work.weixin.qq.com/wework_admin/frame#contacts
    """

    _init_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    """初始化时的url"""

    def get_contacts_list(self) -> list:
        """
        获取成员列表
        return: 成员的手机号
        """
        eles = self.driver.find_elements(By.XPATH, '//*[@id="member_list"]/tr/td[5]')

        phone_list = []
        for ele in eles:
            phone_list.append(ele.text)
        # 不在页面断言
        return phone_list
