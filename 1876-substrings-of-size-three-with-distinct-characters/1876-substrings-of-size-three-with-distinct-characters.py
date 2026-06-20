class Solution(object):
    def countGoodSubstrings(self, s):
        ans=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                temp=[]
                for k in range(i,j+1):
                    temp+=[s[k]]
                if len(temp)==3 and len(set(temp))==3:
                    ans+=1
        return ans
        