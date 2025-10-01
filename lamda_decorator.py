
# higher order function is a funciton which takes a function as an argument
# decorator: adds functionality to a function without changing its code

def valid_int_only(fun):
    def wrapper(inparrg1,inparg2):
        if type(inparrg1) == int and type(inparg2) == int:
            print("before the fuction executed ******")
            return fun(inparrg1,inparg2)
            print("Afterr the fuction executed ******")
        else:
            print("Please enterr a valid integers")
    return wrapper

@valid_int_only
def mult(inp1,inp2):
    return inp1 * inp2
   
@valid_int_only
def addt(inp1,inp2):
    return inp1 + inp2

# result = mult("abc","abcd")
# rersult2 = addt("xyz",5)
# print(result)
# print(rersult2)

result = mult(12,10)
rersult2 = addt(5,10)
print(result)
print(rersult2)


# lambda function: anonymus function which take n input argument and has 1 expression  
# def mult(inp1,inp2):
#     return inp1 * inp2

multlamda = lambda inp1, inp2: inp1 * inp2


addlamda = lambda inp1, inp2: inp1 + inp2

print(multlamda(1,2))
print(addlamda(10,5))


















