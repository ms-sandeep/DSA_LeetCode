class Solution(object):
    def numberOfSubstrings(self, s):
        left=0
        ans=0
        dic={'a':0, 'b':0, 'c':0}
        n=len(s)
        for right in range(n):
            dic[s[right]]+=1

            while dic['a']>0 and dic['b']>0 and dic['c']>0:
                ans+=n-right
                dic[s[left]]-=1
                left+=1
        return ans

    