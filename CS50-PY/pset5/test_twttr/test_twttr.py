from twttr import shorten
import string


def test_empty():
    assert shorten() == ""
    assert shorten("") == ""


def test_only_consonants():
    CONSONANTS_U = "BCDFGHJKLMNPQRSTVWXYZ"
    CONSONANTS_L = "bcdfghjklmnpqrstvwxyz"
    assert shorten(CONSONANTS_U) == "BCDFGHJKLMNPQRSTVWXYZ"
    assert shorten(CONSONANTS_L) == "bcdfghjklmnpqrstvwxyz"


def test_only_vowels():
    VOWELS_U = "AEIOU"
    VOWELS_L = "aeiou"
    assert shorten(VOWELS_U) == ""
    assert shorten(VOWELS_L) == ""


def test_numbers_and_punctuations():
    NUMBERS = "0123456789"
    PUNCS = string.punctuation
    assert shorten(NUMBERS) == "0123456789"
    assert shorten(PUNCS) == "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


def test_mix():
    assert shorten("There is at least 1 failure in test!!") == "Thr s t lst 1 flr n tst!!"
    assert shorten("All Passed Successfully!!") == "ll Pssd Sccssflly!!"
