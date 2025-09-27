# palendrome
# "MOM"  "MOM" = palendrome
# "Apple"  "elppA" = not a palendrome


def rev_str(inpstr):
    revstr = ""
    for char in inpstr:
        revstr = char + revstr
    return revstr

def is_palendrome(inp):
    revStr = rev_str(inp)

    if revStr == inp:
        print(revStr, " is Palendrome")
        return True
    else:
        print(revStr, " is not a Palendrome")
        return  False


# is_palendrome("india")
# is_palendrome("malayalam")
# is_palendrome("9898989")
# is_palendrome("1234566543210")










