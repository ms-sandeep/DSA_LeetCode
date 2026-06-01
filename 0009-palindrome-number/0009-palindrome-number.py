class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        i=0
        rev=''
        for i in y:
            rev=i+rev
        if y==rev:
            return True
        else:
            return False
        