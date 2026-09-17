class Solution(object):
    def longestConsecutive(self, nums):
        num_set = set(nums)
        
        max_lenght = 0

        for i in num_set:
            val= i-1
            if val not in num_set:
                cur=i
                lenght = 1
                while cur+1 in num_set:
                    cur+=1
                    lenght+=1
                if lenght >max_lenght:
                    max_lenght=lenght
            # elif val in nums:
            #     skip

        return max_lenght





        # nums.sort()
        # max_len=1
        # count=1

        # for i in range(1,len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i] - nums[i-1] ==1:
        #         count+=1
        #         if count > max_len:
        #             max_len= count
        #     else:
        #         count=1           

        # if not nums:
        #     return 0
        # else:
        #     return max_len
