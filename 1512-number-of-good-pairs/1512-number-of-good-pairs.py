class Solution(object):
    def numIdenticalPairs(self, nums):
        dic={}
        count=0
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for j in dic:
            val=dic[j]
            count+=val*(val-1)//2
        return count
            

        