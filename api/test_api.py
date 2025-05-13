import pytest
import requests

from api.yaml_util import YamlUtil


class TestApi:
    @pytest.mark.parametrize("args",  YamlUtil('test_api.yaml').read_yaml())
    def test_01_api(self,args):
        url = args["request"]["url"]
        params = args["request"]["params"]
        res = requests.get(url, params=params)
        print(res.text)
        #断言
        assert args["validate"]["eq"]["code"] in res.text


if __name__ == '__main__':
    pytest.main()
