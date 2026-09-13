class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}

        for num in arr:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1

        s=set(dic.values())

        if len(s) == len(dic):
            return True
        else:
            return False
        