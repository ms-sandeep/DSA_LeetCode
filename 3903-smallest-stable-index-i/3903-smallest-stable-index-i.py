class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)

        for i in range(n):
            if (max(nums[0:i+1]) - min(nums[i:n])) <= k:
                return i

        return -1

        