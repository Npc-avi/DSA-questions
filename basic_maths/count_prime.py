class Solution:
    def primeUptoN(self, n):
        num=2
        for i in range(1,n+1):
            if i>3 :
                if i%2!=0 and i%3!=0:
                    num = num + 1
                    
        return  num

print(Solution().primeUptoN(int(input("enter the number to find prime upto:"))))