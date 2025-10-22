
# class StringPrograms:

    # def __init__(self,inpstr):
    #     self.inpstr = inpstr

def all_lower(func):
    def wrapper(arg):
        if type(arg) == str:
            arg = arg.lower()
            return func(arg)
        else:
            return "Please provide valid input"
    return wrapper
@all_lower
def reverse_str(inpstr):
    return inpstr[::-1]

@all_lower
def count_rep_chars(inpstr):

#         INDIANA | output = I= 2, A= 2, D =1 N= 1
    tempDict = {}
    for char in inpstr:
        if char in tempDict:
            tempDict[char] = tempDict[char] + 1
        else:
            tempDict[char] = 1
    return  tempDict


def check_palendrome(inpstr):
    return reverse_str(inpstr) == inpstr
