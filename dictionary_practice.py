# mydict = {"key1": "Python"}
#
# print(mydict)
# mydict["key2"] = "java"
#
# print(mydict)
# mydict["key2"] = "c++"
# print(mydict)
# mydict["key3"] = 25
# print(mydict)
# mydict["key3"] = mydict["key3"] + 5
# print(mydict)
#
# mydict["key2"] = None
# print(mydict)

inpstr = "This is python"
#  nohtyp si sihT
# output = "sihT si nohtyp"
#
# words_list = inpstr.split(" ")
# print(words_list)
# output = ""
# outputList = []
# for word in words_list:
#     print(word)
#     word_rev = ""
#     for char in word:
#         word_rev = char + word_rev
#     print("word_rev",word_rev)
#     outputList.append(word_rev)
#     # output = output+ word_rev + " "
# print(output.strip())
# temSTrr = " "
# print(" ".join(outputList))
#
#



inpDict = {
    "kohli":50,
    "SKY" : 10,
    "Dhoni": 30,
    "Rohit": 30,
    "Abhishek": 60
}

totalScore = 0

# totalScore = totalScore + inpDict["kohli"]
# totalScore = totalScore + inpDict["SKY"]
# totalScore = totalScore + inpDict["Dhoni"]
# totalScore = totalScore + inpDict["Rohit"]
# totalScore = totalScore + inpDict["Abhishek"]

allscore = inpDict.values()
allplayers = inpDict.keys()
print(allplayers)
print(allscore)

# for score in allscore:
#     totalScore = totalScore + score

print("Total score",totalScore)

# print("Score of ",inpDict["Abhishek"])
#
myPlayer = ["Abhishek", "Rohit","kohli"]
# print(f"Score of {myPlayer}",inpDict[myPlayer])


for key,value in inpDict.items():
    print(key,value)
    if key not in myPlayer :
        totalScore = totalScore + value

print(totalScore)




















