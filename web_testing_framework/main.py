import os
import pytest

from web_testing_framework.util import allure_util

if __name__ == '__main__':
    # print('====== 执行当前目录下有所符合条件的测试案例 =======')
    # pytest.main(['-v', '-s'])
    # pytest.main()

    # print('====== 指定执行 test_pytest.py 下的测试类 TestDemo1 =======')
    # pytest.main(['-k','TestDemo1', 'test_pytest.py'])

    # print('====== 指定执行 test_pytest.py 下的测试类 TestDemo1 TestDemo2 =======')
    # pytest.main(['-k','TestDemo1 or TestDemo2', 'test_pytest.py'])

    # print('====== 指定执行test_pytest.py 文件下的 test_02 方法 和 TestDemo2 类下的 test_21 方法 =======')
    # pytest.main(['-k', 'test_02 or TestDemo2 and test_21', 'test_pytest.py'])

    # print('====== 执行 bao 目录下的测试用例 =======')
    # pytest.main(['bao/'])

    print('====== 执行 bao 目录下的测试用例 =======')
    # pytest.main(['-k', 'test_department.py', 'testcase/'])
    # # allure generate ./result -o ./report --clean
    # os.system('allure generate ./result -o ./report --clean')
    # # allure open ./report/
    # os.system('allure open ./report/')
    # os.close()

    allure_util.execute_test_case('test_contacts.py')
    allure_util.open_report()
