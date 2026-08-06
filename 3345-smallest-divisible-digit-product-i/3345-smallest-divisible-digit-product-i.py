class Solution(object):
    def smallestNumber(self, n, t):

        def check(num):
            product = 1

            while num > 0:
                digit = num % 10
                product *= digit
                num //= 10

                if product == 0:
                    break

            return product % t == 0

        while not check(n):
            n += 1

        return n