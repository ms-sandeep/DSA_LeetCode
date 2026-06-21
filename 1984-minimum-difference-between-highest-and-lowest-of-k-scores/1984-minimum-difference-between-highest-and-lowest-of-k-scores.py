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
                ans=min(ans,last_val-frist_val)
        return ans
    

















        # nums.sort()
        # ans=float('inf')
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         temp=[]
        #         for m in range(i,j+1):
        #             temp.append(nums[m])
        #             if len(temp)==k:
        #                 first_val=temp[0]
        #                 last_val=temp[-1]
        #                 ans=min(ans,last_val-first_val)
        # return ans
        