import pytest
import requests

from api.yaml_util import YamlUtil


class TestApi:
    @pytest.mark.parametrize("args", YamlUtil('test_api_post.yaml').read_yaml())
    def test_post_api(self, args):
        if args["request"]["method"] == "POST":
            url = args["request"]["url"]
            json = args["request"]["json"]
            res = requests.post(url, json=json)  # post用json,get用params
            print(f"\n\n请求URL: {url} \n请求参数: {json} \n状态码: {res.status_code} \n响应内容: {res.text} ")
            # 断言
            assert res.json().get('code') == args['validate'][0]['eq']['code']
            print(f"实际code: {res.json().get('code')},预期code: {args['validate'][0]['eq']['code']}")

    @pytest.mark.parametrize("args", YamlUtil('test_api_get.yaml').read_yaml())
    def test_get_api(self, args):
        if args["request"]["method"] == "GET":
            url = args["request"]["url"]
            params = args["request"]["params"]
            res = requests.post(url, params=params)
            print(f"\n\n请求URL: {url} \n请求参数: {params} \n状态码: {res.status_code} \n响应内容: {res.text} ")
            #  断言
            assert res.text.split(",")[1] == args['validate'][0]['eq']['code']
            print(f"实际code: {res.text.split(",")[1]},预期code: {args['validate'][0]['eq']['code']} ")


if __name__ == '__main__':
    pytest.main()
