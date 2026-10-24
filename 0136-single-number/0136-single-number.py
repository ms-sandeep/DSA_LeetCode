class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic = {}

        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        for key, val in dic.items():
            if val == 1:
                return key
        return -1
        