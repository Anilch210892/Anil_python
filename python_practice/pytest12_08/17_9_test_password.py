
# test_password_verification.py

import pytest
from password_verification import verify_password

@pytest.mark.parametrize("password, expected_result", [
    ("Passw0rd", True),   # Valid password
    ("short", False),     # Less than 8 characters
    ("ALLLOWERCASE", False),  # No lowercase letters
    ("12345678", False),  # No uppercase letters or lowercase letters
    ("P@ssword", False),  # No numeric digit
])
def test_password_verification(password, expected_result):
    result = verify_password(password)
    assert result == expected_result

def test_empty_password():
    result = verify_password("")
    assert result == False

def test_valid_special_characters():
    result = verify_password("P@ssw0rd")
    assert result == True

def test_invalid_special_characters():
    result = verify_password("Password123")
    assert result == False
