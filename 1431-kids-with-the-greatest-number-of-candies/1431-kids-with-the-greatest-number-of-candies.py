class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_can=max(candies)
        result=[]
        for i in candies:
            if (i + extraCandies) >= max_can:
                result.append(True)
            else:
                result.append(False)
        return result