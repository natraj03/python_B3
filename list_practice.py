# name1 = "jeet"
# name2 = "soumya"
# name_str3 = "abhijeet"
# # #
# # #
name_list = ["jeet",name2,"biswajeet",name_str3]
# # print(name_list)
# name_list.append("krushna")
# name_list.append(1234)
# # print(name_list)
# # name_list.pop()
# # print(name_list)
# # name_list.remove("krushna")
# # name_list.remove("soumya")
# # print(name_list)
print(name_list[3])
# # name_list.append("soumya")
# # name_list.append("soumya")
# # name_list.append("soumya")
# # name_list.append("soumya")
# # print(name_list)
# # tem_name = name_list[2]
# # print(tem_name)
# # name_list.insert(2,"ravi")
# # print(name_list)
# # #
# batch2 = ["rashmi", "rajesh", "satya"]
#
# # for item in batch2:
# #     name_list.append(item)
# #
# # print(name_list)
#
# name_list.extend(batch2)
# print(name_list)
# #
# name_list[0] = "Apple"
# #
# print(name_list)
# name_list.pop(5)
# # print(name_list)
# name_list.clear()
# print(name_list)
# #

addList = [1,5,2,3,4,5,7,4,2,3,1]
uniqueList =  []
#
for temitem in addList:
    if temitem not in uniqueList:
        uniqueList.append(temitem)
    else:
        print(temitem)


result = 0
# print(addList)
# print("Unnique values=",uniqueList)
# # for item in uniqueList:
# #     result = result + item
# print("result",result)
#
# for item in addList:
#     if item not in uniqueList:
#      uniqueList.append(item)
#      result = result + item
# print("Unnique values=",uniqueList)
#
# print(result)
print("=-=-=-=-=-=-add items of 2 diff list and result stor in 3rrd list--------")

addList2 = [1,5,3,6,4,7,83,6,4,7,8]
addlist3 = [1,2,3,6,4,7,8,1]
#
# # resultList = [2,7,6,12....4,7,8]
resultList = []
#
maxLength = 0
#
if len(addList2) > len(addlist3):
    maxLength =  len(addList2)
else:
    maxLength = len(addlist3)

for index in range(maxLength):

    if len(addList2) > index and len(addlist3) > index:
        resultList.append(addList2[index] + addlist3[index])
    elif len(addList2) > index:
        resultList.append(addList2[index])
    elif len(addlist3) > index:
        resultList.append(addlist3[index])
print("addlist3  ",addlist3)
print("addlist2  ",addList2)
print("resultList",resultList)



