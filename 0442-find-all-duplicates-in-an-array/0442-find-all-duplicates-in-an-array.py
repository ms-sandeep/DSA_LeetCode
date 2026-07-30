class Solution(object):
    def findDuplicates(self, nums):
        seen=set()
        ans=[]
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                ans.append(i)
        return ans
        