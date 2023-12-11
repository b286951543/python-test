import random

from automated_testing_framework.apis.enterprise_wechat_api import EnterpriseWechat


class Department(EnterpriseWechat):
    """
    部门管理
    """

    def create(self):
        """
        部门创建
        :return: 创建结果
        """
        json = {
            "name": f'test_{random.randint(100, 999999)}',
            "parentid": 1
        }
        url = 'cgi-bin/department/create'
        # json 会自动放入请求体
        res = self.enterprise_wechat_send('post', url, json=json)
        return res
