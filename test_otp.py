import pytest
from otp import generate_otp

def test_otp_length():
    otp = generate_otp()
    assert len(otp) == 6

def test_otp_digits():
    otp = generate_otp()
    assert otp.isdigit()

def test_custom_length():
    otp = generate_otp(8)
    assert len(otp) == 8

def test_invalid_length():
    with pytest.raises(ValueError):
        generate_otp(3)

def test_maximum_length():
    with pytest.raises(ValueError):
        generate_otp(11)