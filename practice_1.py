

def countCharrs(inputStr):
    # input = "malayalam"
# m=2, a= 4, l=2 y=1

    tempDict = {}

    for char in inputStr:

        if char in tempDict:
            tempDict[char] = tempDict[char] + 1
        else:
            tempDict[char] = 1

    return tempDict



