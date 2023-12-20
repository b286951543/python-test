from selenium.webdriver.common.by import By

from web_testing_framework_new.base.base import Base
from web_testing_framework_new.page.contacts_list import ContactsListPage


class ContactsAddPage(Base):
    """
    添加成员页面
    https://work.weixin.qq.com/wework_admin/frame#contacts
    """

    __username_input = (By.XPATH, '//*[@id="username"]')
    """姓名"""

    __acctid_input = (By.XPATH, '//*[@id="memberAdd_acctid"]')
    """账户"""

    __phone_input = (By.XPATH, '//*[@id="memberAdd_phone"]')
    """手机号"""

    __save_btn = (By.CSS_SELECTOR, '.js_btn_save')
    """保存按钮"""

    # 如果在这个页面实例化, 会修改 Base 里 _init_url 变量的值
    _init_url = 'https://work.weixin.qq.com/wework_admin/frame#contacts'
    """初始化时的url"""

    def contacts_add(self, data) -> ContactsListPage:
        """
        添加成员操作
        data: 参数
        return: 成员列表页面
        """
        self.load_locator('contacts_add_page_info.yaml', data)
        # # 姓名
        # self.send_keys(self.__username_input, text=username)
        # # 账号
        # self.send_keys(self.__acctid_input, text=acctid)
        # # 手机号
        # self.send_keys(self.__phone_input, text=phone)
        # # 保存
        # self.click(self.__save_btn)
        # 返回成员列表页面
        return ContactsListPage(self.driver)

    def contacts_add_empty_username_fail(self, username, acctid, phone) -> str:
        """
        反例: 添加成员操作
        输入空的姓名
        username: 姓名
        acctid: 账号
        phone: 手机号
        return: 报错内容
        """
        # 姓名
        self.send_keys(self.__username_input, text=username)
        # 账号
        self.send_keys(self.__acctid_input, text=acctid)
        # 手机号
        self.send_keys(self.__phone_input, text=phone)
        # 保存
        self.click(self.__save_btn)
        # 请填写姓名
        ele = self.find_element(By.CSS_SELECTOR, '.ww_compatibleTxt.ww_compatibleTxt_Small.ww_inputWithTips_WithErr > .ww_inputWithTips_tips')
        return ele.text
