from numb3rs import validate


def test_empty():
    assert validate() == False
    assert validate("") == False
    assert validate("...") == False
    assert validate(" . . . ") == False

def test_lessMoreMissingArguments():
    assert validate("1.1") == False
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.2") == False
    assert validate("1.2..4") == False


def test_wrongSeparator():
    assert validate("1,1,1,1") == False
    assert validate("1-1-1-1") == False
    assert validate("1_1_1_1") == False


def test_nonNumeric():
    assert validate("A.B.C.D") == False
    assert validate("AA.BB.CC.DD") == False
    assert validate("i.think.it.crushed") == False
    assert validate("A.10.20.30") == False
    assert validate("?.!.^./") == False


def test_outOfRange():
    assert validate("-1.-1.-1.-1") == False
    assert validate("-1.0.50.3") == False
    assert validate("50.256.27.94") == False
    assert validate("256.256.256.256") == False
    assert validate("0.0.1984.0") == False


def test_acceptable():
    assert validate("0.0.0.0") == True
    assert validate("1.1.1.1") == True
    assert validate("254.254.254.254") == True
    assert validate("255.255.255.255") == True
    assert validate("45.87.230.0") == True
