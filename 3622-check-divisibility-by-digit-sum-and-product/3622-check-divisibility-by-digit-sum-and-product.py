class Solution(object):
    def checkDivisibility(self, n):
        total = 0
        product = 1
        temp = n

        while temp > 0:
            rem = temp % 10
            temp //= 10
            total += rem
            product *= rem

        return n % (total + product) == 0


        
        



        