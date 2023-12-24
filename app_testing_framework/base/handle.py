import allure


def warp(func):
    """
    执行方法后异常的截图功能的扩展类
    用于装饰有返回值的方法
    """
    def inner(*args, **kwargs):
        """
        失败截图的装饰器内部类
        """
        from web_testing_framework.base.base import Base
        base_obj: Base = args[0]  # 获取调用时的第一个参数, 即 self 参数
        try:
            # 需要有返回值
            return func(*args, **kwargs)
        except:
            # 截图保存到测试报告
            allure.attach(base_obj.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            # base_obj.save_img(f'{func.__class__.__name__}_{time.time()}.png')

    return inner


def warp_raise_err(func):
    """
    执行方法后异常的截图功能的扩展类
    用于装饰有返回值的方法
    捕获异常后会继续往外抛出
    """
    def inner(*args, **kwargs):
        """
        失败截图的装饰器内部类
        """
        from web_testing_framework.base.base import Base
        base_obj: Base = args[0]  # 获取调用时的第一个参数, 即 self 参数
        try:
            # 需要有返回值
            return func(*args, **kwargs)
        except:
            # 截图保存到测试报告
            allure.attach(base_obj.driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
            func_name = func.__name__  # 方法名
            class_name = func.__qualname__.split(".")[0]  # 类名
            raise Exception(f'{class_name} {func_name} error')
            # base_obj.save_img(f'{func.__class__.__name__}_{time.time()}.png')

    return inner