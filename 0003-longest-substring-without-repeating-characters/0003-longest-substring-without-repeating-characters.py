class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l=0
        set1=set()
        res=0

        for r in range(len(s)):
            if s[r] not in set1:
                set1.add(s[r])
                res=max(res, r-l+1)
            else:
                while s[r] in set1:
                    set1.remove(s[l])
                    l+=1
                set1.add(s[r])
                res=max(res, r-l+1)
        return res
        