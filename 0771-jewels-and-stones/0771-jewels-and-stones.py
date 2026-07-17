class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        # dic={}
        # for i in jewels:
        #     if i not in dic:
        #         dic[i]=0
        # count=0
        # for j in stones:
        #     if j in dic:
        #         dic[j]+=1
        #         count+=1
        # return count

        #------------------------------------

        # ans=0
        # for i in stones:
        #     if i in jewels:
        #         ans+=1
        # return ans

        #----------------------------------

        count=0
        for i in jewels:
            for j in stones:
                if i==j:
                    count+=1
        return count
        