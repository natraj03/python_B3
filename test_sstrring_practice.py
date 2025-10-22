from  string_practice import reverse_str, count_rep_chars


def test_erverse():
    assert reverse_str(12345) == "Please provide valid input"
    assert reverse_str(["tesst"]) == "Please provide valid input"
    assert reverse_str(1234.55) == "Please provide valid input"
    assert reverse_str("ABC") == "cba"
    assert reverse_str("abc") == "cba"


def test_countChars():
    assert count_rep_chars(1234) == "Please provide valid input"
    result_dict = count_rep_chars("INDIANA")
    assert result_dict["i"] == 2
    assert result_dict["d"] == 1
    assert result_dict["a"] == 2




