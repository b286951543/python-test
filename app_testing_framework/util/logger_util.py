"""
日志
"""

import logging
import os


class Log:
    def log(self):
        """
        日志打印
        """
        root_path = os.path.dirname(os.path.dirname(__file__))
        # 创建 logger 对象
        logger = logging.getLogger(__name__)

        if logger.handlers:  # 只实例化一次
            return logger

        # 获取 log 文件夹路径
        file_path = os.sep.join([root_path, 'log'])
        print('日志文件路径:', file_path)
        # 如果文件夹不存在则创建
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        # 日志格式
        # 参考: https://docs.python.org/zh-cn/3/library/logging.html
        log_formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s - %(funcName)s line:%(lineno)d [%(levelname)s]:\n%(message)s')

        # 文件
        file_handler = logging.FileHandler(filename=file_path + '/api_test.log', encoding='utf-8')
        file_handler.setFormatter(log_formatter)
        # 控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(log_formatter)
        # 设置生效
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
        # 设置日志等级
        logger.setLevel(logging.INFO)
        return logger
