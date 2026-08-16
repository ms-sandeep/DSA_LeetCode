class Solution(object):
    def sortArray(self, nums):
        
        def merge(nums, low, mid, high):
            i=low
            j=mid+1
            lst=[]

            while i<=mid and j<=high:
                if nums[i]< nums[j]:
                    lst.append(nums[i])
                    i+=1
                else:
                    lst.append(nums[j])
                    j+=1
            while i<=mid:
                lst.append(nums[i])
                i+=1
            
            while j<=high:
                lst.append(nums[j])
                j+=1

            for k in range(len(lst)):
                nums[low+k]=lst[k]
                
        def mergeSort(nums, low, high):
            if low==high:
                return
            
            mid=(low + high) // 2

            mergeSort(nums, low, mid)
            mergeSort(nums, mid+1, high)
            merge(nums, low, mid, high)
        mergeSort(nums, 0, len(nums)-1)

        return nums
        
        