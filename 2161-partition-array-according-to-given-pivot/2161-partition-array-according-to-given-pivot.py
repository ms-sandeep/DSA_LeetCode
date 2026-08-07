class Solution(object):
    def pivotArray(self, nums, pivot):
        small_no=0
        equal_no=0
        great_no=0
        
        for i in nums:
            if i > pivot:
                great_no+=1
            elif i == pivot:
                equal_no+=1
            else:
                small_no+=1
        i=0
        j=small_no
        k=small_no+equal_no
        res=[0]*len(nums)
        for num in range(len(nums)):
            if nums[num] < pivot:
                res[i]=nums[num]
                i+=1
            elif nums[num] == pivot:
                res[j]=nums[num]
                j+=1
            else:
                res[k]=nums[num]
                k+=1
        return res
                
        