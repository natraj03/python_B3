
import pytest

@pytest.fixture
def list_ofNum():
    mylist = [1,3,4,5,6,2]

    return mylist


def test_add_list_of_num(list_ofNum):
    tempresult = 0
    for item in list_ofNum:
        tempresult = tempresult + item

    print("addition",tempresult)


def test_mult_list_of_num(list_ofNum):
    tempresult = 0
    for item in list_ofNum:
        tempresult = tempresult * item

    print("Mutiply",tempresult) 


def test_sub_list_of_num(list_ofNum):
    tempresult = 0
    for item in list_ofNum:
        tempresult = tempresult - item

    print("substraction",tempresult) 







