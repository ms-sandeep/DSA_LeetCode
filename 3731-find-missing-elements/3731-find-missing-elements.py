class Solution(object):
    def findMissingElements(self, nums):
        missing=[]

        for i in range(min(nums), max(nums)):
            if i not in nums:
                missing.append(i)
        
        return missing