class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)

        total = n*(n+1)/2
        
        actual =0
        for i in nums:
            actual +=i
        
        

        missing= total - actual

        return missing
    
        
        