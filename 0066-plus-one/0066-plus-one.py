class Solution(object):
    def plusOne(self, digits):
        st=''
        ls=[]
        for i in digits:
            st+=str(i)

        st=int(st)+1
        for j in str(st):
            ls+=[int(j)]
        return ls