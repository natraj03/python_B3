# CRUD: Create, Read, Update, Delete

# #create
# list1 = []
# list2 = ["apple","ball", "cat"]
# print(list2)
#
# myset = {}
# myset2 = {"test1","news","bat"}
# print(myset2)
#
# mytuple = ()
# mytuple2 = ("test11","channel",1234,1234,"test11")
# print(mytuple2)
#
# # read:
# myListitem = list2[1]
# myTupleitem = mytuple2[1]
#
# #  mutability : add and delete
#
#
# list2.append(1234)
# list2.append("moon")
#
# myset2.add(6546)
# myset2.add("sun")
#
#
# print(list2)
# print(myset2)
# print(mytuple2)
#
# list2.append("moon")
# myset2.add("sun")
# print("Duplication-----")
# print(list2)
# print(myset2)
# print(mytuple2)


# input = [1,2,3,4,5]
# output = 15
#
# inputList = (1,2,3,4,5,6,10,1,2,3,4,5)
# uniqueList = []
# result = 0
#
# for item in inputList:
#     if item not in uniqueList:
#         result = result + item
#         uniqueList.append(item)
#
# print("--result--",result)
#
# myset1 = set(inputList)
# result2 = 0
# for item in myset1:
#     result2 = result2 + item
# print("result2",result2)

#  input list of 2 arrays add each and show the result in another array
# list1 = [1,2,3,4,5]
# list2 = [7,8,9,1,2,3,7]
# result_list = [8,10,12,5,8,3,7]
# list duplicates allowed or not?

# list1 = {1,2,3,4,5,3,7}
# list2 = [7,8,9,1,2]
# result_list = []
#
# max_range = 0
# if len(list1) > len(list2):
#     max_range = len(list1)
# else:
#     max_range = len(list2)
#
# for index in range(max_range):
#
#     if index < len(list1) and index < len(list2):
#         result_list.append(list1[index] + list2[index])
#     elif index < len(list1):
#         result_list.append(list1[index])
#     elif index < len(list2):
#         result_list.append(list2[index])
# print("---final list rresult",result_list)

#
# list1 = [1,2,3,4,5,1,2,3,4]
# list2 = [6,7,8,9,0]
#
# # resultList = [0,1,2,3,4,5,6,7,8,9]
# list1.extend(list2)
# resultList = set(list1)

# for item in  list1:
#     resultList.append(item)
#
# for item in  list2:
#     resultList.append(item)
#
# print("final result ",resultList)
#
#
# set1 = {1,2,3,4,5,1,2,3,4}
# set2 = {6,7,8,9,0,1,2,3,4,5}
#
# set3 = set1.union(set2)
# set4 = set1.intersection(set2)
# print("Final set union",set3)
# print("Final set intersection",set4)


itemList= [9,3,25,5,6,17,19,24]

largestNum1 = 0
larrgestNum2 = 0

for item in itemList:
    if largestNum1 < item:
        largestNum1 = item

for item in itemList:
    if largestNum1 != item and larrgestNum2 < item :
        larrgestNum2 = item

print(largestNum1)
print(larrgestNum2)

























