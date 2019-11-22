import pytest
import requests


def test_act3_authentication1():
    # Test 1: Logs into the application successfully
    credentials = {'username': 'admin', 'password': 'admin'}
    login = requests.post("http://localhost:5000/login", data=credentials)
    assert login.status_code == 200 and "Welcome" in login.text


def test_act3_authentication2():
    # Test 2: Tries to log into the application with wrong password and fails
    credentials = {'username':'admin', 'password': 'password'}
    login = requests.post("http://localhost:5000/login", data=credentials)
    assert login.status_code == 200 and "Welcome" in login.text


def test_act3_authentication3():
    # Test 3: Tries to log into the application with wrong username and fails
    credentials = {'username': 'username', 'password': 'admin'}
    login = requests.post("http://localhost:5000/login", data=credentials)
    assert login.status_code == 200 and "Welcome" in login.text


def test_act4_content():
    # Logs into the account successfully
    session = requests.session()
    credentials = {'username': 'admin', 'password': 'admin'}
    login = session.post("http://localhost:5000/login", data=credentials)
    assert login.status_code == 200 and "Welcome" in login.text

    # Uploads a new video
    file = {'file': open("Test_Videos/SampleVideo_1280x720_1mb.mp4", "rb")}
    file_upload = session.post("http://localhost:5000/upload", files=file)
    assert file_upload.status_code == 200
    # Access/Make sure video exists
    video_check = session.get("http://localhost:5000/vids/SampleVideo_1280x720_1mb.mp4")
    assert video_check.status_code == 200

    # Deletes the video
    delete_video = session.get("http://localhost:5000/del/1")
    assert delete_video.status_code == 200

def test_act5_sql_injection():
    pass

    # TODO
    # Vulnerable to classic SQL

    # TODO
    # Vulnerable to blind SQL


def test_act6_ssrf():
    pass
    # TODO
    # Vulnerable to SSRF


def test_act7_command_injection():
    pass

    # TODO
    # Vulnerable to Command Injection


if __name__ == '__main__':
    pytest.main(['-r', 'P'])
