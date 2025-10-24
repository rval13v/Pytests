import pytest


@pytest.fixture
def set_up():
    print("Вход в систему выполнен")

def test_sednind_mail_1(set_up):
    print("Письмо отправлено")


def test_sednind_mail_2(set_up):
    print("Письмо отправлено")

