class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = 0
        max_idx = 0

        for i in range(n):
            if nums[i] < nums[min_idx]:
                min_idx = i

            if nums[i] > nums[max_idx]:
                max_idx = i

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        from_left = right + 1

        from_right = n - left

        from_both = (left + 1) + (n - right)

        return min(from_left, from_right, from_both)
        