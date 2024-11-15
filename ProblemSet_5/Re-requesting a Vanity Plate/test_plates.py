# ////////////////////////////////////////
# //                                    //
# // Name: AAQIL AHMED KULLDIK MANEGAR  //
# //                                    //
# // Assignment: Vanity Plates Test     //
# //                                    //
# ////////////////////////////////////////
from plates import is_valid

# // Testing the is_valid function
def test_is_valid():
    assert is_valid("CS50")
    assert not is_valid("H")
    assert not is_valid("AI2.14")
    assert not is_valid("thistoolong")
    assert not is_valid("AAA22A")
    assert not is_valid("CS05")
    assert not is_valid("57EED")
    assert not is_valid("32")

# check50 cs50/problems/2022/python/tests/plates
# submit50 cs50/problems/2022/python/tests/plates
