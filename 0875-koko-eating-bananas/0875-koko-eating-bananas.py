class Solution(object):
    def speed(self,n,piles):
        total=0
        for i in piles:
            total+=(i+n-1)//n
        return total
    def minEatingSpeed(self, piles, h):
        low=1
        high=max(piles)
        ans=-1
        while (low<=high):
            mid=(low+high)//2
            if (self.speed(mid,piles)<=h):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans           
        
        