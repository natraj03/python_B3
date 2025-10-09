

#  inputlist = [1,2,3,4,5,"a", "b","c", "@","#","$]
#output = l1 = [1,2,3,4,5,6]
# l2 = ["a","b","c"]

def clean_list(fun):

    def wrapper(mylist):
        temp_list = []
        for item in mylist:
            if (type(item) != float)  and (type(item) == int or item.isalpha()):
                temp_list.append(item)
        
        fun(temp_list)
    return wrapper

@clean_list
def seperate_int_and_str(inputList):
    temp_intList = []
    temp_charList = []

    for item in inputList:
        if type(item) == int:
            temp_intList.append(item)
        elif type(item) == str:
            temp_charList.append(item)
    
    print(temp_intList,temp_charList)



seperate_int_and_str([1,2,3,4,"@","A","B","AVSDFASFSA", "&",1.5,"$"])














