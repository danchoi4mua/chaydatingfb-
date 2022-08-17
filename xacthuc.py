import pyotp

def layma2fa(ma):
    totp = pyotp.TOTP(ma)
    return  totp.now()


