import pytest
import requests

from api.yaml_util import YamlUtil


class TestApi:
    @pytest.mark.parametrize("args", YamlUtil('test_api.yaml').read_yaml())
    def test_01_api(self, args):
        url = args["request"]["url"]
        json = args["request"]["json"]
        res = requests.post(url, json=json)  # get用params
        print(f"状态码: {res.status_code}\n响应内容: {res.text}\n请求URL: {url}\n请求参数: {json}")  # ✔️ 中文标签

        # 断言
        # assert args["validate"]["eq"]["code"] in res.text


if __name__ == '__main__':
    pytest.main()
