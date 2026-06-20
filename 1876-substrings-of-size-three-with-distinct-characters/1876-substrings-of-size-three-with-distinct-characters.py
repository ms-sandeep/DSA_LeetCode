class Solution(object):
    def countGoodSubstrings(self, s):
        l=0
        lst=[]
        ans=0
        for r in range(len(s)):
            lst.append(s[r])
            if (r-l==3):
                lst.pop(0)
                l+=1
            if (r-l+1==3):
                if len(set(lst))==3:
                    ans+=1
        return ans

        # ans=0
        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         temp=[]
        #         for k in range(i,j+1):
        #             temp+=[s[k]]
        #         if len(temp)==3 and len(set(temp))==3:
        #             ans+=1
        # return ans
        