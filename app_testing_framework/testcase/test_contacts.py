import random
import time

from app_testing_framework.page.index import IndexPage

class TestContacts:
    """
    通讯录功能测试类
    """

    def setup_class(self):
        self.index = IndexPage()

    def test_contacts_add_01(self):
        """
        测试添加成员
        """

        print(f'{time.time()} 开始')
        random_num = random.randint(100000, 999999)

        username = f'test{random_num}'
        phone = f'13466{random_num}'
        # 进入通讯录页面
        print(f'{time.time()} 进入通讯录页面')
        contacts_list_page = self.index.goto_contacts_list()
        # 进入添加成员页面
        print(f'{time.time()} 进入添加成员页面')
        contacts_add_page = contacts_list_page.goto_contacts_add()
        # 进入手动输入添加成员页面
        print(f'{time.time()} 进入手动输入添加成员页面')
        member_add_page = contacts_add_page.goto_member_add()
        # 添加成员操作
        print(f'{time.time()} 添加成员操作')
        contacts_add_page = member_add_page.member_add(username, phone)
        # 获取弹窗内容
        print(f'{time.time()} 获取弹窗内容')
        toast_text = contacts_add_page.get_toast_text()
        print(toast_text)
        assert toast_text == '添加成功'

