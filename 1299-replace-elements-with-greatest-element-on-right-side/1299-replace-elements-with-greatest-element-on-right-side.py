class Solution(object):
    def replaceElements(self, arr):
        n=len(arr)
        rmax=-1
        for i in range(n-1,-1,-1):
            tem=arr[i]
            arr[i]=rmax
            rmax=max(rmax, tem)
        return arr
        