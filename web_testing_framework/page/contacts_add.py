
from selenium.webdriver.common.by import By

from web_testing_framework.base.base import Base


class Contacts_Add(Base):
    """
    添加成员
    https://work.weixin.qq.com/wework_admin/frame#contacts
    """

    def add(self, username, acctid, phone):
        """
        username: 姓名
        acctid: 账号
        phone: 手机号
        """
        # 姓名
        self.__driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
        # 账号
        self.__driver.find_element(By.XPATH, '//*[@id="memberAdd_acctid"]').send_keys(acctid)
        # 手机号
        self.__driver.find_element(By.XPATH, '//*[@id="memberAdd_phone"]').send_keys(phone)
        # 保存
        self.__driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
