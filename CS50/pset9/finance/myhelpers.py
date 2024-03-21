import string


ACCEPTABLES = string.ascii_letters + string.digits
MIN_LENGTH = 4
MAX_LENGTH = 15

def password_validity_check(text):
    if MIN_LENGTH > len(text) > MAX_LENGTH:
            return False
    for char in text:
            if char not in ACCEPTABLES:
                return False
    return True


def username_validity_check(text):
    for char in text:
        if char not in ACCEPTABLES:
            return False
    return True
