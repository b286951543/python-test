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
