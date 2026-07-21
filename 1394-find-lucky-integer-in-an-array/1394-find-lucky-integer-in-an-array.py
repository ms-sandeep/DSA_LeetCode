class Solution(object):
    def findLucky(self, arr):
        dic={}
        ans=-1
        for i in range(len(arr)):
            if arr[i] not in dic:
                dic[arr[i]]=1
            else:
                dic[arr[i]]+=1
        for j in dic:
            if dic[j]==j:
                if j>ans:
                    ans=j
        return ans
        