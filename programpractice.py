
# print("this is index 1")
# print("this is index 2")

# find a given string is palendrome or not
# input = "malayalam"
# output = "is palendrome"
# input = "Mango"
# output = "Not a palendrome"


def reverseSTR(inpstr):
    result = inpstr[:2:-1]
    return  result

def checkPalendrome(inputstr):

    if reverseSTR(inputstr) == inputstr:
        return True
    else:
        return False



def test_palendrrome():
    # none
    # assert checkPalendrome(None) == False, "Assertion failed: for None as an argument"

    # single character
    assert checkPalendrome("12122a") == True
    # case sensitive
    assert checkPalendrome("Malayalam") == False

    # with numbers
    assert checkPalendrome("12321") == True
    assert checkPalendrome("malayalam") == True
    assert checkPalendrome("MALAYALAM") == True


def revstr():
    pass




