import random

from automated_testing_framework.apis.enterprise_wechat_api import EnterpriseWechat


class Department(EnterpriseWechat):
    """
    部门管理
    """

    def create(self, counter_example_data=None):
        """
        部门创建
        传入反例数据时,会自动覆盖正例数据
        :param counter_example_data: 反例数据
        :return: 创建结果
        """
        json = {
            "name": f'test_{random.randint(100, 999999)}',
            "parentid": 1
        }
        url = 'cgi-bin/department/create'
        # json 会自动放入请求体
        res = self.enterprise_wechat_send('post', url, json=json, counter_example_data=counter_example_data)
        return res
