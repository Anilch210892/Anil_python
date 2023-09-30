import pytest
import re


# Function to verify if a password meets the specified conditions
def verify_password(password):

    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False

    # Check if the password contains at least one uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check if the password contains at least one lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check if the password contains at least one numeric digit
    if not any(char.isdigit() for char in password):
        return False

    # If all conditions are met, the password is valid
    return True


# Define test cases using pytest.mark.parametrize
@pytest.mark.parametrize("password, expected_result", [
    ("Passw0rd", True),  # Valid password
    ("short", False),  # Less than 8 characters
    ("ALLLOWERCASE", False),  # No lowercase letters
    ("12345678", False),  # No uppercase letters or lowercase letters
    ("P@ssword", False),  # No numeric digit
    ("Ravitejafuckoff", True)  # Exempted password
])
def test_password_verification(password, expected_result):
    assert verify_password(password) == expected_result


# Run the tests
if __name__ == "__main__":
    pytest.main()
