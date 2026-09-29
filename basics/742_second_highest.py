class Solution:
    def secondMostFrequentElement(self, nums):
        arr={}
        for num in nums:
            if num in arr:
                arr[num]+=1
            else:
                arr[num]=1
        
        highest_num = 0
        highest_fre = 0

        for num,count in arr.items():
            if count>highest_fre:
                highest_num=num
                highest_fre=count
            elif count==highest_fre and num<highest_num:
                highest_num=num
            
        second_num = -1
        second_fre = -1

        for num,count in arr.items():
            if count==highest_fre:
                    continue
            if count>second_fre:
                second_fre=count
                second_num=num
            elif count==second_fre and num<second_num:
                second_num=num

        return second_num
            