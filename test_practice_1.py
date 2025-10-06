from practice_1 import countCharrs


def test_allsamalls():
    result_dict = countCharrs("india")
    assert result_dict["i"] == 2
    assert result_dict["n"] == 1
    assert result_dict["d"] == 1
    assert result_dict["a"] == 1


def test_all_caps():
    result_dict = countCharrs("INDIA")
    assert result_dict["I"] == 2
    assert result_dict["N"] == 3
    assert result_dict["D"] == 1
    assert result_dict["A"] == 1

def test_alpha_numeric():
    result_dict = countCharrs("INDIA121")
    assert result_dict["I"] == 2
    assert result_dict["N"] == 1
    assert result_dict["D"] == 1
    assert result_dict["A"] == 1
    assert result_dict["1"] == 2
    assert result_dict["2"] == 1

