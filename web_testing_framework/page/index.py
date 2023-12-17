from selenium.webdriver.common.by import By

from web_testing_framework.base.base import Base
from web_testing_framework.page.contacts_add import Contacts_Add


class Index(Base):
    """
    首页
    https://work.weixin.qq.com/wework_admin/frame#index
    """

    def goto_contacts_add(self):
        """
        进入添加成员页面
        """
        self.__driver.find_element(By.XPATH, '//span[text()="添加成员"]').click()
        # 返回添加成员页面
        return Contacts_Add()
