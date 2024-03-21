from plates import is_valid


def test_empty():
    assert is_valid() == False
    assert is_valid("") == False


def test_lenght():
    assert is_valid("A") == False
    assert is_valid("AAABBBC") == False
    assert is_valid("AAABBBCCC") == False
    assert is_valid("AA") == True
    assert is_valid("AAA") == True
    assert is_valid("AAABBB") == True


def test_punc():
    assert is_valid("!AAAA") == False
    assert is_valid("A-AAA") == False
    assert is_valid("AAAA?") == False
    assert is_valid("AAAA.") == False


def test_startWithNonAlphabetic():
    assert is_valid("1AAA") == False
    assert is_valid("43AA") == False


def test_alphabeticAfterNumeric():
    assert is_valid("AA12AA") == False
    assert is_valid("AA1A2") == False
    assert is_valid("AA1A2B") == False


def test_firstNumericIsZero():
    assert is_valid("ANY01") == False
    assert is_valid("AN00") == False
    assert is_valid("AN021") == False


def test_acceptables():
    assert is_valid("AAA") == True
    assert is_valid("AAA123") == True
    assert is_valid("BDC12") == True
    assert is_valid("AA50") == True
    assert is_valid("LST101") == True
