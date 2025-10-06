
# inp1 = 5
# inp2 = 10

# print(inp1 + inp2)

class claculator:

    def add_num(self, inp1, inp2):
        print(inp1 + inp2)

    def mul_num(self, inp1, inp2):
        print(inp1 * inp2)

    def sub_num(self, inp1, inp2):
        print(inp1 - inp2)
    @staticmethod
    def mystaticMethod(zyz):
        print(zyz)

claculator_obj = claculator()


claculator_obj.add_num(5,10)

claculator_obj.mul_num(5,10)

claculator_obj.sub_num(5,10)
claculator.sub_num(5,10)
claculator.mystaticMethod("with classs testing **********")
claculator_obj.mystaticMethod("wiht obj testing **********")



class string_operatoons:
    def revStr(inp1):
        print(inp1[::-1])
    

string_operatoons_obj = string_operatoons()
string_operatoons_obj.revStr("hello") 



def add_listofInt(inpList):
    temresult = 0
    for item in inpList:
        temresult = temresult + item
    print(temresult)
add_listofInt([1,2,3,4,5,6])









