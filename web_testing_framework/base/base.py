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

    def __init__(self):
        self.__driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()))
        self.__driver.implicitly_wait(60)  # 隐式等待时间
        self.__driver.maximize_window()
        self.__driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookie_path = os.path.join(os.path.dirname(__file__), 'cookies.yaml')
        if os.path.exists(cookie_path):
            with open(cookie_path, 'r', encoding='utf-8') as f:
                cookies = yaml.safe_load(f)
            if cookies:
                for cookie in cookies:
                    self.__driver.add_cookie(cookie)
                self.__driver.refresh()
        if '<a id="logout" class="frame_operation_link" href="javascript:;">退出</a>' not in self.__driver:  # 如果页面没有退出, 即没有登录
            self.__driver.find_element(By.XPATH, '//*[@id="menu_index"]')  # 等待这个元素出现(等待登录)
            cookies = self.__driver.get_cookies()  # 获取 cookies 并保存
            with open(cookie_path, 'w', encoding='utf-8') as f:
                yaml.safe_dump(cookies, f)
