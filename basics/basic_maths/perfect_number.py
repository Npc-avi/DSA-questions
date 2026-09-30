class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False 
        z=1
        for i in range (2,int(num**0.5)+1):
            if num%i==0:
                z+=i
                if i!=(num//i):
                    z+=(num//i)
        return z==nun

num = int(input("enter the number to check perfect number:"))
if Solution().checkPerfectNumber(num)