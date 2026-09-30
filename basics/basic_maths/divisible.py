x = int(input("enter the number:"))
sorted=[]
for i in range(1,int(x**0.5)+ 1):
    if x%i==0:
        sorted.append(i)
        if x//i != i:
            sorted.append(x//i)
    else:
        continue
sorted.sort()
print("The factors of the number are:",sorted)
