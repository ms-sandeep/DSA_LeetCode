class Solution(object):
    def generate(self, numRows):
        res=[]
        for i in range(numRows):
            lst=[]
            for j in range(i+1):
                if j==0 or j==i:
                    lst.append(1)
                else:
                    sum_val=res[i-1][j-1]+res[i-1][j]
                    lst.append(sum_val)
            res.append(lst)
        return res
        