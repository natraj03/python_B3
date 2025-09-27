# # test = set()
# #
# # test.add("abcd")
# # test.add("1234")
# # test.add(5678)
# # test.add(5678)
# # test.add("1234")
# #
# # mylist = ["abcd", "1234", 5678, "1234", 5678]
# # print(test)
# # print("list",mylist[2])
# #
# # for item in test:
# #     print(item)
# #
# #
# # # test.remove(56782)
# # test.discard(5678)
# # test.discard("abcd")
# # if "abcd" not in test:
# #     print("item abcd not found")
# # print(test)
# #
# # removed_item = test.pop()
# # test.clear()
# # print("removed_item",removed_item,test)
# #
# #
#
# set1 = {15,1,2,10,9}
# set2 = {4,5,6,1,2}
# set4 = {"a","b","c","s"}
# set3 = set1.union(set2)
# print("Set",set3)
# print("Set",set1.intersection(set2))
# print("Set 4",set1.union(set2,set4))
# print("difference", set1.difference(set2))
# print("systematic difference", set1.symmetric_difference(set2))
#
#

inp_list = [1,2,4,5,6,5,4,3,2]
add_all_numbers = 0
for item in inp_list:
    add_all_numbers = add_all_numbers + item

print(add_all_numbers)

onlyunique = 0

uniqueItems = set(inp_list)
for item in uniqueItems:
    onlyunique = onlyunique + item

print("uniqueItems",onlyunique)
toupe1 = tuple()
tuple111 = (1,2,"123454433",4,5,6,2,5,6)
print("tuple111",tuple111)
print("tuple111",tuple111[2])

list2 = [1,2,3,4,5,7,5,4,22,7]
list1 = [1,3,2,1,4,5,3,22,4,7,3,12]
# result =[2,5,5,5,7,5,4]
result = []

# maxLoop = len(list2) # 7
# if maxLoop < len(list1): # list1 =5
#     maxLoop = len(list1)  # skip
#
# for index in range(maxLoop):
#     if index < len(list1) and index < len(list2):
#         result.append(list1[index] + list2[index])
#     elif index < len(list2):
#         result.append( list2[index])
#     elif index < len(list1):
#         result.append(list1[index])
# print("result",result)


print(len(list1) - len(list2))

















