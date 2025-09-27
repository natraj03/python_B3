from function_prractice import  multi

def test_multipliction():

    result = multi(6,6)
    assert result == 36

    result2 = multi(6, -6)
    assert result2 == -36

    result3 = multi(-6, -6)
    assert result3 == 36

    result4 = multi(0, -6)
    assert result4 == 0

def test_multipliction2():

    result = multi(7,6)
    assert result == 42


    result2 = multi(7, -6)
    assert result2 == -36

