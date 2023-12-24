from appium.webdriver.common.appiumby import AppiumBy

from app_testing_framework.base.base import Base

class MemberAddPage(Base):
    """
    手动输入添加成员页面
    """

    __username_input = (AppiumBy.XPATH, '(//android.widget.EditText)[1]')
    """用户名"""

    __phone_input = (AppiumBy.XPATH, '(//android.widget.EditText)[2]')
    """手机号"""

    __save_btn = (AppiumBy.XPATH, '//*[@text="保存"]')
    """保存按钮"""

    def member_add(self, username, phone):
        """
        添加成员操作
        """
        self.send_keys(*self.__username_input, username)
        self.send_keys(*self.__phone_input, phone)
        self.click(*self.__save_btn)

        # 添加成员页面

        from app_testing_framework.page.contacts_add import ContactsAddPage
        return ContactsAddPage(self.driver)
