import pytest
import requests


def test_Hello_World():
    resp = requests.get('http://127.0.0.1:8080')
    assert 'Hello World' in resp.text
    assert 200 == resp.status_code


if __name__ == '__main__':
    pytest.main()
