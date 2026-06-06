class Solution(object):
    def maxDistance(self, colors):
        n=len(colors)
        ans=0
        for i in range (n):
            for j in range (i+1,n):
                if colors[i]!=colors[j]:
                    temp=j-i
                    ans=max(ans, temp)
        return ans
        