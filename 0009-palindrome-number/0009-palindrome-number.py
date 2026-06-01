class Solution(object):
    def isPalindrome(self, x):
        y=str(x)
        rev=''
        for i in y:
            rev=i+rev
        if y==rev:
            return True
        else:
            return False
        