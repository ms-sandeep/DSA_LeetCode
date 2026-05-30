class Solution(object):
    def isPalindrome(self, s):
        r=''
        for i in s:
            if i.isalnum():
                r=i.lower()+r
        frev=r[::-1]
        if frev==r:
            return True
        else:
            return False
        
        