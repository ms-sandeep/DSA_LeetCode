class Solution(object):
    def smallestIndex(self, nums):
        result = float('inf')

        for i in range(len(nums)):
            val = nums[i]
            digit_sum = 0

            while val > 0:
                digit_sum += val % 10
                val //= 10

            if digit_sum == i:
                result = i
                break

        return result if result != float('inf') else -1

                    

            
        