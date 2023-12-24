from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver

from app_testing_framework.base.handle import warp, warp_raise_err
from app_testing_framework.util.logger_util import Log


class Base:
    """
    所有页面的基类
    """

    def __init__(self, driver=None):
        self.logger = Log().log()

        if driver is not None:
            self.driver: WebDriver = driver
            return

        config = {
            # 设备名
            'platformName': 'Android',
            # 设备版本
            'platformVersion': '9',  # adb -s 127.0.0.1:51572 shell getprop ro.build.version.release
            # 设备名称
            'deviceName': '127.0.0.1:52370',
            # 软件包名 企业微信
            'appPackage': 'com.tencent.wework',
            # adb -s 127.0.0.1:51299 shell dumpsys window windows | findstr mFocusedApp
            # 软件启动页 企业微信首页
            'appActivity': '.launch.LaunchSplashActivity',
            # adb -s 127.0.0.1:51572 shell dumpsys window windows | findstr mFocusedApp
            # 允许中文输入
            'unicodeKeyboard': True,
            'resetKeyboard': True,
            # 关闭软件时不清除缓存数据, 不配置的话, 会把登录之类的信息清空
            'noReset': True
        }
        # 4723是 Appium Server GUI 打开时的端口号, wd/hub 是固定的写法
        self.driver = webdriver.Remote(r'http://127.0.0.1:4723/wd/hub', desired_capabilities=config)
        self.driver.implicitly_wait(15)

    @warp  # 装饰器
    def find_element(self, by, location=None):
        """
        查找单个元素
        by: 定位方式
        location: 定位内容
        """

        self.logger.info(f'查找元素: 方式: {by}, 元素: {location}')

        if location:  # 传入了两个参数
            return self.driver.find_element(by, location)
        if isinstance(by, tuple) and len(by) == 2:  # 只传入了 by, 且 by 是元组, 长度为2
            return self.driver.find_element(*by)  # 解包
        raise ValueError('查找单个元素时, by 参数有误:', by)

    @warp_raise_err
    def find_element_with_raise_err(self, by, location=None):
        """
        查找单个元素
        如果报错,会往外抛出异常
        by: 定位方式
        location: 定位内容
        """

        self.logger.info(f'查找元素2: 方式: {by}, 元素: {location}')

        if location:  # 传入了两个参数
            return self.driver.find_element(by, location)
        if isinstance(by, tuple) and len(by) == 2:  # 只传入了 by, 且 by 是元组, 长度为2
            return self.driver.find_element(*by)  # 解包
        raise ValueError('查找单个元素时, by 参数有误:', by)

    @warp
    def find_elements(self, by, location=None):
        """
        查找多个元素
        by: 定位方式
        location: 定位内容
        """

        self.logger.info(f'查找多个元素: 方式: {by}, 元素: {location}')

        if location:  # 传入了两个参数
            return self.driver.find_elements(by, location)
        if isinstance(by, tuple) and len(by) == 2:  # 只传入了 by, 且 by 是元组, 长度为2
            return self.driver.find_elements(*by)  # 解包
        raise ValueError('查找多个元素时, by 参数有误:', by)

    def click(self, by, location=None, swipe_switch=False, num=3, duration=500):
        """
        点击
        swipe_switch: 是否滑动点击, false: 否, true: 滑动点击
        """

        if swipe_switch:  # 滑动查找到元素后点击
            self.swipe_find(by, location, num, duration).click()
            self.logger.info(f'点击元素 {location}')
            return

        self.find_element(by, location).click()

    def send_keys(self, by, location=None, text=None):
        """
        填写输入框
        """

        ele = self.find_element(by, location)
        ele.clear()  # 清空默认值
        ele.send_keys(text)
        self.logger.info(f'输入文本: {text}')

    def get_text(self, by, location=None):
        """
        获取元素的文本内容
        """
        self.logger.info(f'获取文本: 方式: {by}, 元素: {location}')
        return self.find_element(by, location).text

    def get_toast_text_by_class(self):
        """
        第一种获取 toast 内容的方式
        """
        return self.get_text(AppiumBy.XPATH, '//*[@class="android.widget.Toast"]')

    def get_toast_text_by_contains(self):
        """
        第二种获取 toast 内容的方式
        """
        return self.get_text(AppiumBy.XPATH, '//*[contains(@text,"Clicked popup")]')

    def get_move_position(self, width, height) -> tuple:
        """
        获取滑动的起始/结束坐标
        """
        start_x = width / 2  # 起始 x 轴
        end_x = width / 2  # 结束 x 轴

        start_y = height * 0.8  # 起始 y 轴
        end_y = height * 0.2  # 结束 y 轴
        return start_x, start_y, end_x, end_y

    def swipe_find(self, by, location, num=3, duration=500):
        """
        滑动查找
        默认滑动查找3次, 耗时500ms
        """
        self.logger.info(f'滑动查找: 方式: {by}, 元素: {location}, 次数:{num}, 滑动时间:{duration}')
        for i in range(num):
            try:
                # 使用会抛出异常的查找元素方法
                ele = self.find_element_with_raise_err(by, location)
                return ele
            except:
                print('没找到元素, 滑动屏幕')
                # 获取屏幕尺寸
                size = self.driver.get_window_size()
                # 获取滑动的起始/结束坐标
                move_position = self.get_move_position(size.get('width'), size.get('height'))
                # 滑动屏幕
                self.driver.swipe(*move_position, duration=duration)

            if i == num - 1:
                raise Exception(f'滑动了 {num} 次, 未找到元素. by: {by}, location: {location}"]')
