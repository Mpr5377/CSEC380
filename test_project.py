import pytest
import requests


def test_act3_authentication():
    x = 5
    y = 5

    assert x != y, "test failed"
    #TODO
    # Test 1: Logs into the application successfully

    #TODO
    # Test 2: Tries to log into the application with wrong password and fails

    #TODO
    # Test 3: Tries to log into the application with wrong username and fails


def test_act4_content():
    pass

    #TODO
    # Logs into the account successfully

    #TODO
    # Uploads a new video

    #TODO
    # Access/Make sure video exists

    #TODO
    # Deletes the video


def test_act5_sql_injection():
    pass

    #TODO
    # Vulnerable to classic SQL

    #TODO
    # Vulnerable to blind SQL


def test_act6_ssrf():
    pass
    #TODO
    # Vulnerable to SSRF


def test_act7_command_injection():
    pass

    #TODO
    # Vulnerable to Command Injection


if __name__ == '__main__':
    pytest.main()