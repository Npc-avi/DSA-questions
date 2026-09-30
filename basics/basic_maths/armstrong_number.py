x = int(input("enter number to check armstrong: "))
org = x
y = 0

while x>0:
    z=x%10
    temp = z**3
    y+=temp
    x=x//10

if y==org:
    print("the number is armstrong")
else:
    print("the number is not armstrong")