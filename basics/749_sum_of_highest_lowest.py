class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        arr={}
        for num in nums:
            if num in arr:
                arr[num]+=1
            else:
                arr[num]=1

        highest_num=0
        highest_fre=0
        lowest_num=0
        lowest_fre=float('inf')

        for num, count in arr.items():
            if highest_fre<count:
                highest_fre=count

        for num, count in arr.items():
            if lowest_fre>count:
                lowest_fre=count

        z = highest_fre+lowest_fre

        return z

