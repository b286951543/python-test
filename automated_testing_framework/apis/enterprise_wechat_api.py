from automated_testing_framework.protocol.http_protocol import HttpClient
from automated_testing_framework.utils.yaml_util import read_config_yaml


class EnterpriseWechat:
    """
    企业微信初始化类\n
    包含获取 token
    """

    def __init__(self):
        """
        这里的 HttpClient 不建议使用继承, 因为这个类使用继承可能会出现一些问题
        建议使用初始化的方式
        这个类实例化时会自动执行这里的方法
        """

        # 获取不同环境的配置信息
        self.__env = read_config_yaml('env.yaml')['env']
        print('当前使用的配置是', self.__env)
        properties_config = read_config_yaml('properties.yaml')
        self.__enterprise_wechat_host = properties_config['enterprise_wechat_host'][self.__env]
        self.__corp_id = properties_config['corp_id'][self.__env]
        self.__corp_secret = properties_config['corp_secret'][self.__env]

        # 实例化 HttpClient
        self.__http_client = HttpClient()
        # 获取 token
        self.__token = self.__get_token()

    def __get_token(self):
        """
        获取 token
        :return:
        """
        params = {
            'corpid': self.__corp_id,
            'corpsecret': self.__corp_secret
        }
        # 获取token
        url = 'cgi-bin/gettoken'
        result = self.__http_client.send('get', self.__enterprise_wechat_host + url, params=params)
        return result.json()['access_token']

    def enterprise_wechat_send(self, method, url, **kwargs):
        """
        企业微信发送请求通用接口
        :param method:
        :param url:
        :param kwargs:
        :return:
        """
        if kwargs.get('params'):
            kwargs['params']['access_token'] = self.__token
        else:
            kwargs['params'] = {'access_token': self.__token}

        res = self.__http_client.send(method, self.__enterprise_wechat_host + url, **kwargs)
        return res
