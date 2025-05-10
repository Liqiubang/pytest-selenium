import pytest
import requests


class TestApi:
    def test_01_api(self):
        url = 'https://www.bejson.com/validators/yaml_editor/'
        params = {
            'name': "name",
            'age': 18
        }
        res = requests.get(url, params=params)
        print(res.text)


if __name__ == '__main__':
    pytest.main()
