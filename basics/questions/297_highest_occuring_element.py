class Solution:
    def mostFrequentElement(self, nums):
        min = {}
        for num in nums:
            if num in min:
                min[num]+=1
            else:
                min[num]=1
        
        most = 0
        val = 0

        for num, count in min.items():
            if count>most:
                most=count
                val = num
            elif count==most and num<val:
                val=num
        return val
                
