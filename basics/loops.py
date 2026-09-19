number = int(input("enter a number you want to factorial: "))
factorial = 1
for i in range(1,number+1):
    factorial = factorial*i
    number = number-1
print("factorial of the number is : ",factorial)