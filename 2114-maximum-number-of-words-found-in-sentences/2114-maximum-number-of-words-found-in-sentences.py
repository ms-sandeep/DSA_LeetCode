class Solution(object):
    def mostWordsFound(self, sentences):
        lst=[]
        for i in sentences:
            c=1
            for j in i:
                if j==' ':
                    c+=1
            lst+=[c]
        return max(lst)

        