import os

import yaml
from jsonpath_ng import parse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# from webdriver_manager.chrome import ChromeDriverManager
from web_testing_framework_new.base.handle import warp
from web_testing_framework_new.util.logger_util import logger


class Base:
    """
    所有页面的基类
    """

    _init_url = ''
    """初始化时的url"""

    def __init__(self, driver=None):
        """
        登录
        """
        if driver is not None:
            self.driver = driver
            return

        # 这里的变量不能私有化, 否则子类会不好获取
        # 获取驱动器
        # self.__driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        driver_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'chrome_driver', 'chromedriver.exe')
        self.driver = webdriver.Chrome(service=Service(executable_path=driver_path))

        self.driver.implicitly_wait(15)  # 隐式等待时间
        self.driver.maximize_window()
        self.driver.get(self._init_url)

        # cookies 路径
        cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.yaml')
        if os.path.exists(cookie_path):  # 有cookies ,则添加
            with open(cookie_path, 'r', encoding='utf-8') as f:
                cookies = yaml.safe_load(f)
            if cookies:
                for cookie in cookies:
                    self.driver.add_cookie(cookie)
                self.driver.refresh()

        # 如果上面的 cookies 失效了, 下面的逻辑可以重新登录
        # 页面没登录或登录失效, 则重新登录
        if '<a id="logout" class="frame_operation_link" href="javascript:;">退出</a>' not in self.driver.page_source:  # 如果页面没有退出, 即没有登录
            self.driver.find_element(By.XPATH, '//*[@id="menu_index"]')  # 等待这个元素出现(等待登录)
            cookies = self.driver.get_cookies()  # 获取 cookies 并保存
            with open(cookie_path, 'w', encoding='utf-8') as f:
                yaml.safe_dump(cookies, f)

    @warp  # 装饰器
    def find_element(self, by, location=None):
        """
        查找单个元素
        by: 定位方式
        location: 定位内容
        """
        if location:  # 传入了两个参数
            return self.driver.find_element(by, location)
        if isinstance(by, tuple) and len(by) == 2:  # 只传入了 by, 且 by 是元组, 长度为2
            return self.driver.find_element(*by)  # 解包
        raise ValueError('查找单个元素时, by 参数有误:', by)

    def find_elements(self, by, location=None):
        """
        查找多个元素
        by: 定位方式
        location: 定位内容
        """
        if location:  # 传入了两个参数
            return self.driver.find_elements(by, location)
        if isinstance(by, tuple) and len(by) == 2:  # 只传入了 by, 且 by 是元组, 长度为2
            return self.driver.find_elements(*by)  # 解包
        raise ValueError('查找多个元素时, by 参数有误:', by)

    def click(self, by, location=None):
        """
        点击
        """
        self.find_element(by, location).click()

    def send_keys(self, by, location=None, text=None):
        """
        填写输入框
        """
        ele = self.find_element(by, location)
        ele.clear()  # 清空默认值
        ele.send_keys(text)

    def get_text_list(self, by, location=None) -> list:
        """
        获取文本内容的列表
        return: 内容组成的列表
        """
        eles = self.find_elements(by, location)

        text_list = []
        for ele in eles:
            text_list.append(ele.text)
        # 不在页面断言
        return text_list

    # def save_img(self, img_name):
    #     """
    #     保存截图
    #     """
    #     img_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img', img_name)
    #     print('截图为', img_path)
    #     self.driver.save_screenshot(img_path)

    def load_locator(self, yaml_file, data=None):
        yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'locator', yaml_file)
        with open(yaml_path, 'r', encoding='utf-8') as f:
            steps = yaml.safe_load(f)
            for step in steps:
                by = step.get('by')
                location = step.get('location')
                action = step.get('action')
                logger.info(f'开始操作元素: by:{by}, location:{location}, action:{action}')
                if action == 'send_keys':  # 说明时输入
                    if data is not None:  # 有传 data, 说明需要把 yaml 里面的值替换成data里面对应的值
                        if step.get('text') in data.keys():  # yaml 里面的text的内容, 在 data 里面作为key
                            # 把 yaml 里面的 text 的值替换成 data 里面 text 的值
                            new_step = self.replace_val('$..text', step, data[step.get('text')])
                            logger.info(f'输入文本: text:{new_step.get("text")}')
                            self.send_keys(by, location, new_step.get('text'))
                            # 下面适用与 yaml 文件只有一层的情况
                            # self.send_keys(by, location, data[step.get['text']])
                    else:  # 有传入 data, 说明需要替换
                        logger.info(f'输入文本: text:{step.get("text")}')
                        self.send_keys(by, location, step.get('text'))
                else:
                    # 通过反射调用本类的方法
                    getattr(self, action)(by, location)

    def replace_val(self, jsonpath_expr, data, value):
        p = parse(jsonpath_expr)
        return p.update(data, value)