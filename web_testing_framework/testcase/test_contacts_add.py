import random
import time

from web_testing_framework.page.index import IndexPage


class TestContactsAdd:
    def setup_class(self):
        self.index = IndexPage()

    def test_contacts_add_01(self):
        """
        测试添加成员
        """
        random_num = random.randint(100000, 999999)

        username = f'test{random_num}'
        acctid = f'test{random_num}'
        phone = f'13466{random_num}'
        # 首页进入 添加成员页面
        contacts_add_page = self.index.goto_contacts_add()
        # 成员列表页面 添加成员
        contacts_list_page = contacts_add_page.contacts_add(username, acctid, phone)
        # 进入列表页面
        contacts_list = contacts_list_page.get_contacts_list()
        print(contacts_list)
        time.sleep(500)
        assert phone in contacts_list

    def test_contacts_add_empty_username_fail(self):
        """
        反例: 测试添加成员
        姓名为空
        """
        random_num = random.randint(100000, 999999)

        acctid = f'test{random_num}'
        phone = f'13466{random_num}'
        # 首页进入 添加成员页面
        contacts_add_page = self.index.goto_contacts_add()
        # 成员列表页面 添加成员
        result_value = contacts_add_page.contacts_add_empty_username_fail('', acctid, phone)
        # 进入列表页面
        print(result_value)
        # str 为不可变数据类型, 可直接比较
        assert '请填写姓名' == result_value
