from um import count


def test_empty():
    assert count() == 0
    assert count("") == 0


def test_notExist():
    assert count("Nope, it is not here") == 0


def test_existInSubstring():
    assert count("yummy album, um.any umbrella umm num") == 1


def test_acceptables():
    assert count("Um um, UM") == 3


def test_mix():
    assert count("Um, thanks for the um... album. ") == 2
