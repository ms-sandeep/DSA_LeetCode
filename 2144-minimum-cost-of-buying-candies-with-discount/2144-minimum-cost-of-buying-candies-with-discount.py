class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        ans=0
        took=0
        for i in range(len(cost)-1,-1,-1):
            if took==2:
                took=0
            else:
                took+=1
                ans+=cost[i]
        return ans
        