from seasons import calculate, validate
from datetime import date
import pytest


def test_validate():
    # CORRECT USAGE IS : YYYY-MM-DD
    with pytest.raises(SystemExit) as info: validate()
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("January 1, 1999")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("any-number-here")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("06-07-1845")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("2000-00-00")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("1789-13-2")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("1645-2-32")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("0914-12-84")
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: validate("2000.00.00")
    assert str(info.value) == "Invalid date"

    assert validate("1658-3-01") == (1658, 3, 1)
    assert validate("2023-12-2") == (2023, 12, 2)
    assert validate("1700-07-25") == (1700, 7, 25)


def test_calculate():
    today_for_test = date(2023, 12, 2)
    tomorrow = date(2023, 12, 3)
    future_day = date(2589,1,1)
    yesterday = date(2023,12,1)
    historical_day = date(1923, 10, 29)
    someday = date(2000, 4, 16)

    assert calculate(today_for_test, today_for_test) == "Zero"

    with pytest.raises(SystemExit) as info: calculate(tomorrow, today_for_test)
    assert str(info.value) == "Invalid date"

    with pytest.raises(SystemExit) as info: calculate(future_day, today_for_test)
    assert str(info.value) == "Invalid date"

    assert calculate(yesterday, today_for_test) == "One thousand, four hundred , forty"
    assert calculate(historical_day, today_for_test) == "Fifty-two million, six hundred, forty-four thousand, nine hundred , sixty"
    assert calculate(someday, today_for_test) == "Twelve million, four hundred, twenty-seven thousand, two hundred"
