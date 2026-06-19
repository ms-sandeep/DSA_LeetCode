class Solution(object):
    def plusOne(self, digits):
        cary=1
        for i in range(len(digits)-1,-1,-1):
            sum_val=digits[i]+cary
            digits[i]=sum_val%10
            cary=sum_val/10
        if cary==1:
            digits=[1]+digits
        return digits