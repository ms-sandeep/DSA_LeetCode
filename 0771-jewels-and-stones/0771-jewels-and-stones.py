class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        dic={}
        for i in jewels:
            if i not in dic:
                dic[i]=0
        count=0
        for j in stones:
            if j in dic:
                dic[j]+=1
                count+=1
        return count