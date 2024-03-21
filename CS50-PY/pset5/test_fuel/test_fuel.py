from fuel_v1 import convert, gauge
import pytest


def test_convertHasSlash():
    with pytest.raises(ValueError):
        convert("1-4")
        convert("3.7")
        convert("28")


def test_convertFloat():
    with pytest.raises(ValueError):
        convert("1.8/3")
        convert("2/4.5")
        convert("6.3/7.4")


def test_convertNonNumeric():
    with pytest.raises(ValueError):
        convert("A/B")
        convert("1/B")
        convert("A/4")


def test_convertNegativeNumbers():
    with pytest.raises(ValueError):
        convert("-1/-2")
        convert("1/-4")
        convert("-3/5")


def test_convertCompareNomDenom():
    with pytest.raises(ValueError):
        convert("2/1")
        convert("7/4")
    assert convert("5/5") == 100


def test_convertZeroDivision():
    with pytest.raises(ZeroDivisionError):
        convert("7/0")


def test_convertAccuracy():
    assert convert("1/2") == 50
    assert convert("0/6") == 0
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/2") == 100


def test_gaugeIsInteger():
    with pytest.raises(ValueError):
        gauge("A")
        gauge("?")
        gauge("4.6")


def test_gaugeEmpty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gaugeFull():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gaugeAnyValue():
    assert gauge(2) == "2%"
    assert gauge(10) == "10%"
    assert gauge(33) == "33%"
    assert gauge(98) == "98%"
