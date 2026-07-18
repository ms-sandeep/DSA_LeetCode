class Solution(object):
    def findGCD(self, nums):
        min_v=min(nums)
        max_v=max(nums)
        ans=0
        for i in range(1,max_v+1):
            if min_v%i==0 and max_v%i==0:
                if i>ans:
                    ans=i
        return ans
        