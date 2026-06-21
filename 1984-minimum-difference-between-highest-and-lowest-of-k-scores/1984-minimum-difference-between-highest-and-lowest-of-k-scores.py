class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        ans=float('inf')
        l=0
        temp=[]
        for r in range(len(nums)):
            temp.append(nums[r])
            if r-l==k:
                temp.pop(0)
                l+=1
            if r-l+1==k:
                frist_val=temp[0]
                last_val=temp[-1]
                ans=min(ans,temp[-1]-temp[0])
        return ans
        