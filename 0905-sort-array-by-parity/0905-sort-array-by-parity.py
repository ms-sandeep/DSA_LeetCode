class Solution(object):
    def sortArrayByParity(self, nums):
        for i in range(len(nums)-1):
            index=i
            for j in range(i+1,len(nums)):
                if nums[j]%2==0:
                    index=j
            nums[i], nums[index] =nums[index], nums[i]
        return nums
        