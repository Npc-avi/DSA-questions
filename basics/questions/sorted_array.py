    def arraySortedOrNot(self, arr, n):
        if len(arr)<2:
            return True
        else:
            for i in range(n-1):
                if arr[i]>arr[i+1]:
                    return False
                
            return True
    
