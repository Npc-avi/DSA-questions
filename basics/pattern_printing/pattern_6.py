x = int(input("enter a number to print the pattern: "))

for i in range(x):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*x-(2*i+1)):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    print()


