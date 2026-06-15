class Solution(object):
    def rearrangeArray(self, nums):
        pos=[]
        neg=[]
        for i in nums:
            if i>0:
                pos+=[i]
            else:
                neg+=[i]

        k=0
        for j in range(len(pos)):
            nums[k]=pos[j]
            nums[k+1]=neg[j]
            k+=2
        return nums
        