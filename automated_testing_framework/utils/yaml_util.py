import yaml
import os.path

root_path = os.path.dirname(os.path.dirname(__file__))


def read_data_yaml(file_name):
    path = os.path.join(root_path, 'data', file_name)
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data


def read_config_yaml(file_name):
    path = os.path.join(root_path, 'config', file_name)
    print('当前使用的配置文件是', path)
    with open(path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
        return data
