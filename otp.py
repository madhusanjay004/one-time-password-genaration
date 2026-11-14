import secrets

def generate_otp(length=6):

    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError("Length must be an integer")

    if length < 4 or length > 10:
        raise ValueError("OTP length must be between 4 and 10")

    otp = ''.join(
        str(secrets.randbelow(10))
        for _ in range(length)
    )

    return otp


if __name__ == "__main__":
    print("Your OTP is:", generate_otp())