x = int(input("enter the number to count: "))
count = 0
while x>0:
    count += 1
    x=x//10
    print(x)

print("the count of all numbers is: ",count)