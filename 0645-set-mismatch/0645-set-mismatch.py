class Solution(object):
    def findErrorNums(self, nums):
        duplicate=float('-inf')
        missing=float('-inf')
        s=set()
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                duplicate=nums[i]
        for j in range(1,len(nums)+1):
            if j not in s:
                missing=j
        return [duplicate,missing]
        