from programpractice import rev_str, is_palendrome


def test_revstring_fun():
    result = rev_str("INDIA")
    assert result == "AIDNI"
    assert rev_str("98 76") == "67 89"
    assert rev_str("India") == "aidnI"
    assert rev_str("") == ""


# def test_palen():
#     assert is_palendrome("India") == False
#     assert is_palendrome("MALAYALAM") == True
#     assert is_palendrome("india") == False
#     assert is_palendrome("malayalam") == True

def test_palen():
    assert is_palendrome("India") == False
    assert is_palendrome("MALAYALAM") == True
    assert is_palendrome("india") == False
    assert is_palendrome("malayalam") == True



