class modify:
    def plus(self,a):
        a = a+10
        print("value after addition is : ",a)
        return a
    def minus(self,a):
        a = a-10
        print("value aftersubstraction is: ",a)
        return a

modify = modify()

y = int(input("enter the number to perform on: "))

x = int(input("addition(1) and substraction(2): "))

match x:
    case 1:
        modify.plus(y)
        print(y)
    case 2:
        modify.minus(y)
        print(y)
    case _:
        print("invalid input")
    
z = modify.plus(y)
print("after calling the functon to add we get = ",z)

print(x)
print(y)
