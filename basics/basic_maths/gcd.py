n1 = int(input("enter number 1:"))
n2 = int(input("enter number 2:"))
gcd = 0

for i in range(1,min(n1,n2)+1):
    if n1%i==0 and n2%i==0:
        if i>gcd:
            gcd = i

print("the gcd of",n1,"and",n2,"is",gcd)