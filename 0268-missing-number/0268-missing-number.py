class Solution(object):
    def missingNumber(self, nums):
        n=len(nums)
        
        sum=0
        for i in nums:
            sum+=i
        
        n=n*(n+1)/2

        missing=n-sum

        return missing
    
        
        