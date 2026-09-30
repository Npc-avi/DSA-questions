x = int(input("enter a number to check if it is palindrome or not:"))
z = x
rev = 0

while x>0:
    y=x%10
    rev = rev*10 + y
    x=x//10

print(rev)
if rev==z:
    print("the number is palindrome")
else:
    print("the number is not palindrome")