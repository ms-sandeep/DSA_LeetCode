class Solution(object):
    def rearrangeArray(self, nums):
        f=[0]*len(nums)
        p=0
        n=1
        for i in range(len(nums)):
            if nums[i]>0:
                f[p]=nums[i]
                p+=2
            else:
                f[n]=nums[i]
                n+=2
        return f
                



        # pos=[]
        # neg=[]
        # for i in nums:
        #     if i>0:
        #         pos+=[i]
        #     else:
        #         neg+=[i]

        # k=0
        # for j in range(len(pos)):
        #     nums[k]=pos[j]
        #     nums[k+1]=neg[j]
        #     k+=2
        # return nums
        