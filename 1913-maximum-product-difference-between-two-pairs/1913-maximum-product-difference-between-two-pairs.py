class Solution(object):
    def maxProductDifference(self, nums):
        nums.sort()

        a=nums[0]
        b=nums[1]

        c=nums[-1]
        d=nums[-2]

        result=abs((a*b)-(c*d))

        return result