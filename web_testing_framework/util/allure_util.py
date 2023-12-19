import os
import pytest


def execute_test_case(filename):
    """
    执行测试用例
    """
    pytest.main(['-k', filename, 'testcase/'])
    # allure generate ./result -o ./report --clean
    os.system('allure generate ./result -o ./report --clean')


def open_report():
    """
    打开测试报告
    """
    os.system('allure open ./report/')
