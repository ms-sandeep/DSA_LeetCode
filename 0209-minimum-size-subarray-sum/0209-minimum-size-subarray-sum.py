class Solution(object):
    def minSubArrayLen(self, target, nums):
        l=0
        ans=float('inf')
        temp=0
        for r in range(len(nums)):
            temp+=nums[r]

            while temp >= target:
                ans=min(ans,r-l+1)
                temp -=nums[l]
                l+=1
        if ans ==float('inf'):
            return 0
        return ans

        