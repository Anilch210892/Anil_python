

import pytest


@pytest.mark.parametrize()

def test_password_length():
    password = generate_password(8)
    assert len(password) == 8

def test_password_length():
    password = generate_password()
    assert len(password) == 12


def test_password_length():
    password = generate_password()
    assert len(password) ==-6
