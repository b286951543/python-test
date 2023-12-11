import pytest

from automated_testing_framework.apis.department_api import Department
from automated_testing_framework.utils.yaml_util import read_data_yaml


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

    def test_create_depart(self):
        """
        创建部门
        :return:
        """
        res = self.dept_manage.create()
        assert res.json()['errcode'] == 0

    @pytest.mark.parametrize('case', read_data_yaml('department_data.yaml'))
    def test_create_depart_not(self, case):
        """
        创建部门的反例
        :return:
        """
        print(case)