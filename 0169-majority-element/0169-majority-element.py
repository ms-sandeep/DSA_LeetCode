class Solution(object):
    def majorityElement(self, nums):
        dic={}
        temp=len(nums)//2
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            val=dic[j]
            if val>temp:
                return j
        


        