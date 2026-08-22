class Solution(object):
    def checkDivisibility(self, n):
        sum = 0
        product = 1
        temp = n

        while temp>0:
            rem = temp% 10
            temp //= 10
            sum += rem
            product*= rem

        return n % (sum + product) == 0


        
        



        