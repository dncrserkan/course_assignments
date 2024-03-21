from bank import value


def test_empty():
    assert value() == 0
    assert value(" ") == 0


def test_startWithHello():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, there") == 0


def test_start_WithOnlyH():
    assert value("Hey") == 20
    assert value("how are you?") == 20


def test_notStartWithH():
    assert value("Good morning") == 100
    assert value("What's up") == 100


def test_firstCharIsAlphabetic():
    assert value("!Hello") == 0
    assert value("!!Hey") == 20
    assert value("9!Nice") == 100
