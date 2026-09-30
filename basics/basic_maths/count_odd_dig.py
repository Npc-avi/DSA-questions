x = int(input("enter the number to count odd digits:"))

count = 0

while x>0:
    y = x%10
    if y%2!=0:
        count+=1
    x=x//10

print(count)