# class Solution:
#     def trap(self, height: list[int]) -> int:
#         left, right = 0, len(height)-1
#         left_max,right_max=height[left], height[right]
#         water=0

#         while left < right:
#             if left_max < right_max:
#                 left +=1
#                 left_max= max(left_max,height[left])
#                 water += left_max-height[left]
#             else:
#                 right -=1
#                 right_max= max(right_max,height[right])
#                 water += right_max-height[right]
#         return water

class Solution:
    def trap(self, height):
        n = len(height)

        left = [0] * n
        right = [0] * n

        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])

        right[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], height[i])

        water = 0

        for i in range(n):
            water += min(left[i], right[i]) - height[i]

        return water
        
        
        