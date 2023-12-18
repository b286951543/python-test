import requests
import json
from jsonpath_ng import parse

from api_testing_framework.util.logger_util import logger


class HttpClient:

    def send(self, method, url, fail_example_data=None, **kwargs):
        if fail_example_data is not None:
            for key, value in fail_example_data.items():
                # 如果传参有 headers, 把 headers 里面的 key 替换为 value
                if 'headers' in kwargs.keys():
                    self.replace_val(f'$..{key}', kwargs['headers'], value)
                # 如果传参有 params, 把 params 里面的 key 替换为 value
                if 'params' in kwargs.keys():
                    self.replace_val(f'$..{key}', kwargs['params'], value)
                # 如果传参有 json, 把 json 里面的 key 替换为 value
                if 'json' in kwargs.keys():
                    self.replace_val(f'$..{key}', kwargs['json'], value)
                # 如果传参有 data, 把 data 里面的 key 替换为 value
                if 'data' in kwargs.keys():
                    self.replace_val(f'$..{key}', kwargs['data'], value)

        logger.info(f'请求地址: {url}')
        # 将一个字典（kwargs）以JSON格式输出，同时设置缩进为2个空格，并允许非ASCII字符
        logger.info(f'请求参数: \n{json.dumps(kwargs, indent=2, ensure_ascii=False)}')
        res = requests.request(method, url, **kwargs)
        logger.info(f'响应结果: \n{json.dumps(res.json(), indent=2, ensure_ascii=False)}')
        return res

    def replace_val(self, jsonpath_expr, data, value):
        p = parse(jsonpath_expr)
        return p.update(data, value)
