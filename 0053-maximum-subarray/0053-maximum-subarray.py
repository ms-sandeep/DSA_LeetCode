class Solution(object):
    def maxSubArray(self, nums):
        max_val=float('-inf')
        sum_val=0
        for i in range(0,len(nums)):
            sum_val+=nums[i]
            if sum_val>max_val:
                max_val=sum_val
            if sum_val<0:
                sum_val=0
        return max_val














        # max_val=float('-inf')
        # for i in range(len(nums)):
        #     sum_val=0
        #     for j in range(i,len(nums)):
        #         sum_val+=nums[j]
        #         if sum_val>max_val:
        #             max_val=sum_val
        # return max_val        