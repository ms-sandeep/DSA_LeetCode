class Solution(object):
    def isPowerOfTwo(self, n):
        if n==0:
            return False
        x = n & (n-1)

        if(x==0):
            return True
        else:
            return False
        