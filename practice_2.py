#1
#input = "i love python"
#output = "nohtyp evol i"



# tempstr = "this is string"
def reverse_the_string(inpstr):
    outputstr = ""
    for char1 in inpstr:
        outputstr = char1 + outputstr

    return outputstr

# rreverrse1 = reverse_the_string("i love python")


# return2 = reverse_the_string("i love java")

# print(rreverrse1)
# print(return2)
#2
#input = "i love python"
#output = "i  evol nohtyp"
# i
# love
# python

def reverse_words_in_string(inputStr):
    word_list = inputStr.split(" ")
    result = ""
    for item in word_list:
        result = result + reverse_the_string(item) + " "
    print("before strip=",result,"=")
    result = result.strip()
    print("after strip=",result,"=")

    return result

# print(reverse_words_in_string("i love java"))
#
# tempstr = "@@test @@@ testing @@"
# print(tempstr)
# print(tempstr.strip("@"))


def test_reverseStr():
    assert reverse_the_string("python") == "nohtyp"
    assert reverse_the_string("PythoN") == "NohtyP"
    assert reverse_the_string("12345") == "54321"
    assert reverse_the_string("123 45") == "54 321"

def test_check_reverse_words():
    assert reverse_words_in_string("one tow") == "eno wot"
    assert reverse_words_in_string("one three") == "eno eerht"


