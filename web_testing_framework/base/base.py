from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import os
import yaml


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

        self.driver.implicitly_wait(60)  # 隐式等待时间
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
