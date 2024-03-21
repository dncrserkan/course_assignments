from jar import Jar
import pytest


def test_init():
    jar1 = Jar()
    assert jar1.capacity == 12
    jar1 = Jar(10)
    assert jar1.capacity == 10
    with pytest.raises(ValueError, match="Capacity must be positive integer"):
        jar1 = Jar(0)
    with pytest.raises(ValueError, match="Capacity must be positive integer"):
        jar1 = Jar(-1)
    with pytest.raises(ValueError, match="Capacity must be positive integer"):
        jar1 = Jar("10")
    with pytest.raises(ValueError, match="Capacity must be positive integer"):
        jar1 = Jar("ANY")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"



def test_deposit():
    jar2 = Jar()
    jar3 = Jar()
    jar4 = Jar()
    jar2.deposit(1)
    assert jar2.size == 1
    jar3.deposit(2)
    jar3.deposit(3)
    assert jar3.size == 5
    
    with pytest.raises(ValueError, match="n must be positive interger"):
        jar2.deposit()
    with pytest.raises(ValueError, match="n must be positive interger"):
        jar2.deposit(-1)
    with pytest.raises(ValueError, match="n must be positive interger"):
        jar2.deposit(0)
    with pytest.raises(ValueError, match="n must be positive interger"):
        jar2.deposit("ANY")
    with pytest.raises(ValueError, match="too many cookies"):
        jar4.deposit(13)


def test_withdraw():
    jar5 = Jar()
    jar6 = Jar()
    jar7 = Jar()
    jar5.deposit(1)
    jar5.withdraw(1)
    assert jar5.size == 0
    jar6.deposit(5)
    jar6.withdraw(4)
    assert jar6.size == 1
    
    jar5.deposit(4)
    with pytest.raises(ValueError, match="n is not positive or greater than size"):
        jar5.withdraw(5)
    with pytest.raises(ValueError, match="n is not positive or greater than size"):
        jar7.withdraw(13)
    with pytest.raises(ValueError, match="n must be positive integer"):
        jar5.withdraw(-1)
    with pytest.raises(ValueError, match="n must be positive integer"):
        jar5.withdraw(0)
    with pytest.raises(ValueError, match="n must be positive integer"):
        jar5.withdraw("ANY")
