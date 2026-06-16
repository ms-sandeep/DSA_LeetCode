class Solution(object):
    def decodeMessage(self, key, message):
        dic={}
        temp=97
        for i in key:
            if i!=' ' and i not in dic:
                dic[i]=chr(temp)
                temp+=1
        ans=''
        for j in message:
            if j in dic:
                ans+=dic[j]
            else:
                ans+=' '
        return ans
                

        