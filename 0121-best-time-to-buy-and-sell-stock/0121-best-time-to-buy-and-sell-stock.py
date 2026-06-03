class Solution(object):
    def maxProfit(self, prices):
        max_no=prices[0]
        ans=0
        for i in range(1,len(prices)):
            ans=max(ans,(prices[i]-max_no))
            max_no=min(max_no,prices[i])
        return ans
        