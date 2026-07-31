class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        maxOnes=0
        count=0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            
            if count > maxOnes:
                maxOnes = count

        return maxOnes
        