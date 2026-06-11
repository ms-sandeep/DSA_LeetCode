class Solution(object):
    def twoSum(self, nums, target):      
        map={}
        for i in range(len(nums)):
            x =target-nums[i]
            if x in map:
                return i, map[x]
            else:
                map[nums[i]]=i

