# tempvar = 71
# today = "this is string variable"
# var2 = 345
# var3 = 877
# var4 = "78d8f78d7f"
# var1_mult = 55
# var1_mult1 = 55
# b = 75.5

# print(f"Multiplication of 5 * 1 =",5*1)
# print(f"Multiplication of 5 * 2 =",5*2)
# print(f"Multiplication of 5 * 3 =",5*3)
# print(f"Multiplication of 5 * 4 =",5*4)
# print(f"Multiplication of 5 * 5 =",5*5)

#
# print(f"Multiplication of {tempvar} * 1 =",tempvar*1)
# print(f"Multiplication of {tempvar} * 2 =",tempvar*2)
# print(f"Multiplication of {tempvar} * 3 =",tempvar*3)
# print(f"Multiplication of {tempvar} * 4 =",tempvar*4)
# print(f"Multiplication of {tempvar} * 5 =",tempvar*5)
#
# var1 = 5
# var2 = 5.5
#
# print(var1 * var2)
#
# temstr = "welcome to python"
# print(temstr)
#
# print(type(var1),type(var2), type(temstr))
# print(temstr[11])

# str1 = "5"
# str2 = "6"
#
# varint1 = int(str1)
# varint2 = int(str2)
# print(varint2 * varint1)
#
# intvar11 = 5
# temstr = str(intvar11)
# print(intvar11 * 7)
#
# string1 = "hello"
# reverse = string1[4] + string1[3] + string1[0]
#
# var1 = 1
# var2 = 10
# print(var1,var2)
#
# var2 = var1 + var2  # var2 = 11, var1 = 1
# var1 = var2 - var1  # var1 = 10, var2 = 11
# var2 = var2 - var1  # var2 = 1
# print("swap",var1,var2)


# temstr = "hello python"
#
# print(temstr[0])
# print(temstr[1])
# print(temstr[2])

# for index in range(start,stop,step):
# for index in range(1,50,1):
#     print(index)

# resultstr = ""
# for index in range(0,len(temstr),2):
#     print("character",temstr[index])
#     resultstr = temstr[index] + resultstr
# print(resultstr)
#
#
# temstr2 = "hello world"
# revchar = ""
# for char in temstr2:
#     print("character",char)
#     revchar =  char + revchar
# print(revchar)

# range(start,stop,step)
temstrr = "hello"
temResult = ""
print(len(temstrr))
# for index in range( len(temstrr)):
#     temResult =  temstrr[index] + temResult


#
# for index in range(len(temstrr)-1, -1, -1):
#     temResult =  temResult + temstrr[index]

for char in temstrr:
    temResult = char + temResult

print(temResult)

sliceResult = temstrr[len(temstrr)::-1]
print("slice result=",sliceResult)



#
# for index in range(2,10,2):
#     # if index % 2 == 0:
#     #     print(index," is even number")
#
#     print(index," is even number")
#
# for index in range(1,10,2):
#     # if index % 2 == 0:
#     #     print(index," is even number")
#
#     print(index," is odd number")
#
#
#






































