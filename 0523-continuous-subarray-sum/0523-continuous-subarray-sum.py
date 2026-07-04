class Solution(object):
    def checkSubarraySum(self, nums, k):
        dic = {0: -1}
        prf_sum = 0
        
        for i, num in enumerate(nums):
            prf_sum += num
            remainder = prf_sum % k
            
            if remainder in dic:
                if i - dic[remainder] >= 2:
                    return True
            else:
                dic[remainder] = i                
        return False
        