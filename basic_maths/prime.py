x = int(input("enter the number:"))
is_prime = True
if x < 2:
    is_prime = False
else:
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")