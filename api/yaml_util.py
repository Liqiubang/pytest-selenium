import yaml


class YamlUtil:
    # 通过init方法把yaml文件传入这个类
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

    # 读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file, mode='r', encoding='utf-8') as f:
            # 对yaml反序列化，将yaml转化成字典dict格式
            value = yaml.load(f, Loader=yaml.FullLoader)
            print(value, type(value))
            return value


if __name__ == '__main__':
    YamlUtil('test_api_post.yaml').read_yaml()
