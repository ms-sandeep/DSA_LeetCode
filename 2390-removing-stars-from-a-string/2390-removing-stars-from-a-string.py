class Solution(object):
    def removeStars(self, s):
        lst=[]
        for i in s:
            if i == "*":
                lst.pop()
            else:
                lst.append(i)

        result=""
        for j in lst:
            result+=j

        return result

        
        