import pytest
import allure

from automated_testing_framework.apis.department_api import Department
from automated_testing_framework.utils.yaml_util import read_data_yaml


# 设置分层, 1级目录
@allure.epic('企业微信')
# 设置分层, 2级目录
@allure.feature('部门管理')
class TestDepartment:
    """
    部门管理测试
    """

    def setup_class(self):
        """
        实例化部门接口
        :return:
        """
        self.dept_manage = Department()

    @allure.title('创建部门')
    def test_create_depart(self):
        """
        创建部门
        :return:
        """
        res = self.dept_manage.create()
        assert res.json()['errcode'] == 0

    @allure.title('创建部门 反例')
    @pytest.mark.parametrize('case', read_data_yaml('department_data.yaml'))
    def test_create_depart_not(self, case):
        """
        创建部门的反例
        :param case: 测试案例
        :return:
        """
        for key, value in case.items():
            res = self.dept_manage.create(value)
            assert res.json()['errcode'] == value['expect']

    @allure.title('获取子部门ID列表')
    def test_sub_depart(self):
        res = self.dept_manage.get_sub_depart(parent_id=1)
        res_json = res.json()
        id_list = [item['id'] for item in res_json['department_id']]
        self.__depart_id_list = id_list
        assert len(id_list) != 0

    @allure.title('删除部门')
    def test_delete_depart(self):
        self.test_sub_depart()
        # 删除 1号 部门
        self.__depart_id_list.remove(1)
        for depart_id in self.__depart_id_list:
            res = self.dept_manage.delete(depart_id)
            assert res.json()['errcode'] == 0
