x = int(input("enter a number to print the pattern: "))

for i in range(x):
    for j in range(x,i,-1):
        print("*",end=" ")
    print()