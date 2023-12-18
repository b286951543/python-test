import random

from api_testing_framework.api.enterprise_wechat_api import EnterpriseWechat


class Department(EnterpriseWechat):
    """
    部门管理
    """

    def create(self, fail_example_data=None):
        """
        部门创建
        传入反例数据时,会自动覆盖正例数据
        :param fail_example_data: 反例数据
        :return: 创建结果
        """
        json = {
            "name": f'test_{random.randint(100, 999999)}',
            "parentid": 1
        }
        url = 'cgi-bin/department/create'
        # json 会自动放入请求体
        res = self.enterprise_wechat_send('post', url, json=json, fail_example_data=fail_example_data)
        return res

    def get_sub_depart(self, parent_id=1):
        """
        获取子部门ID列表
        :return: 结果
        """
        params = {
            "id": parent_id
        }
        url = 'cgi-bin/department/simplelist'
        # params 会自动放入 url
        res = self.enterprise_wechat_send('get', url, params=params)
        return res

    def delete(self, depart_id):
        """
        删除部门
        :return: 结果
        """
        params = {
            "id": depart_id
        }
        url = 'cgi-bin/department/delete'
        # params 会自动放入 url
        res = self.enterprise_wechat_send('get', url, params=params)
        return res
