class Solution(object):
    def removeDuplicates(self, s):
        res=[]        
        for ch in s:
            if res and res[-1]==ch:
                res.pop()
            else:
                res.append(ch)
        return "".join(res)        