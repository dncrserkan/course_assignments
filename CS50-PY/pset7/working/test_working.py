from working import convert
import pytest

def test_empty():
    with pytest.raises(ValueError):
        convert()
        convert(": AM to : PM")


def test_wrongMeridems():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
        convert("09:00 ZN to 17:00 NX")
        convert("09:00 AM to 17:00 NX")
        convert("09 ZN to 17 PM")


def test_wrongMinutes():
    with pytest.raises(ValueError):
        convert("09:ab AM to 05:-8 PM")
        convert("09:72 AM to 05:400 PM")
        convert("09:2 AM to 05:42 PM")


def test_wrongHours():
    with pytest.raises(ValueError):
        convert("-4:15 AM to 7:20 PM")
        convert("AA:27 AM to 7:40 PM")
        convert("09: AM to 17:42 PM")
        convert("0 AM to 1:00 PM")
        convert("1 AM to 0:00 PM")


def test_wrongSeperator():
    with pytest.raises(ValueError):
        convert("02:34 PM - 8:00 PM") 
        convert("02:34 PM : 8:00 PM") 


def test_acceptables():
    assert convert("09:00 AM to 05:00 PM") == "09:00 to 17:00"
    assert convert("9:40 AM to 5:20 PM") == "09:40 to 17:20"
    assert convert("09:07 AM to 5 PM") == "09:07 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    
    assert convert("1 AM to 3 PM") == "01:00 to 15:00"
    assert convert("12:00 AM to 4:00 PM") == "00:00 to 16:00"
    assert convert("4 AM to 1 PM") == "04:00 to 13:00"
    assert convert("5:00 AM to 12:00 PM") == "05:00 to 12:00"
