class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        res=[]

        while left < right:
            b = right - left
            h = min(height[left] , height[right])
            area= b*h
            res.append(area)

            if height[right] > height[left] :
                left +=1
            else:
                right -=1

        return max(res)


        