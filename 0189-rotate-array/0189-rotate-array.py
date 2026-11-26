class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        res=[0]*n
        for i in range(n):  
            ind=(i+k)%n
            res[ind]=nums[i] 
        for i in range(n):
            nums[i]=res[i]

        # k= k % len(nums)
        # nums = nums[-k:] + nums[:-k]

        return nums
        