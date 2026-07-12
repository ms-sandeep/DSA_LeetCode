class Solution(object):
    def arrayRankTransform(self, arr):
        num=set(arr)
        nums=sorted(num)

        num_to_rank={}
        for i, num in enumerate(nums):
            num_to_rank[num]=(i+1)

        res=[]
        for ele in arr:
            res.append(num_to_rank[ele])
        
        return res
        