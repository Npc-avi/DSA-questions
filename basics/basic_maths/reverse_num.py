x = int(input("enter the number to reverse:"))
rev = 0
while x>0:
    y = x%10
    rev = rev*10 + y
    x = x//10
print("\nReversed number is:",rev)
