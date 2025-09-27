# list

# name1 = "jeet"
# name2 = "soumya"
#
# name_list = ["biswajeet", "raghunath",name2,name1,55, 55, "Apple"]
#
# print(name_list,name1[0])
#
# tempItem = name_list[2]
# print(tempItem,tempItem[0])
# myint = name_list[4]
# print(myint * 2)
# name_list.append("Apple")
# name_list.append("Ball")
# print(name_list)
#
# name_list.pop(5)
#
# print(name_list)
#
# name_list.remove('raghunath')
#
# print(name_list)
#
# name_list.insert(1,"India")
# print(name_list)
# name_list.clear()
# print(name_list)
# # Allows Duplicate
# # Allows Indexing
# # Allows Mutablity


number_list = [1,2,3,4,5,6,6,2,70,7,6,2,6,6,6,7,3,18,19]
# expected output = 21

result = 0

#1 add all integerrs of list
# for item in number_list:
#     result = result + item
#
# print("final result",result)

#2 add only non repeting numbers
# unique_list = []
# backup_list = []
# for item in number_list:
#     if item not in unique_list:
#         unique_list.append(item)
#     backup_list.append(item)
# print("Inique:",unique_list)
# print("backup",backup_list)
# print("original",number_list)
#
#
# for item in unique_list:
#     backup_list.remove(item)
#
# print("Inique:",unique_list)
# print("backup",backup_list)
# print("original",number_list)
#
# for item in number_list:
#     if item not in backup_list:
#         result = result + item
#
# print("result=",result)


# find the biggest number

biggest_number = 0

for item in number_list:
    if item > biggest_number:
        biggest_number = item

print("biggest number",biggest_number)

# number_list = [1,2,3,4,5,6,6,2,70,7,6,2,6,6,6,7,3,18,19]

#3 find the 2nd biggest number
biggest_number2 = 0

for item in number_list:
    if biggest_number != item and item > biggest_number2:
        biggest_number2 = item

print("second biggest number",biggest_number2)

