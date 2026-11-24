class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right =len(nums)-1
        res = [0]*len(nums)
        k=len(res)-1

        while left <= right:
            val1 = nums[left]**2
            val2 = nums[right]**2
            if val1 > val2:
                res[k]=val1
                k-=1
                left += 1
            else:
                res[k]=val2
                k-=1
                right -=1
        return res


        