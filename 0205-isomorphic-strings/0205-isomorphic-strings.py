class Solution(object):
    def isIsomorphic(self, s, t):
        dic={}
        rev={}
        isomorphic=True
        for i in range(len(s)):
            chr1=s[i]
            chr2=t[i]
            if chr1 not in dic and chr2 not in rev:
                dic[chr1]=chr2
                rev[chr2]=chr1
            elif chr1 in dic and dic[chr1]!=chr2:
                isomorphic=False
                break
            elif chr2 in rev and rev[chr2]!=chr1:
                isomorphic=False
                break            
        return isomorphic

        