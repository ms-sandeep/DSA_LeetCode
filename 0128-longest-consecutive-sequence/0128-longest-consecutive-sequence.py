class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()
        max_len=1
        count=1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] - nums[i-1] ==1:
                count+=1
                if count > max_len:
                    max_len= count
                # else:
                #     count=1
            else:
                count=1
           

        if not nums:
            return 0
        else:
            return max_len
