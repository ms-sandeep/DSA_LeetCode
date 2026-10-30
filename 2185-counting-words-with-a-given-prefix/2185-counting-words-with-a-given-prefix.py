class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        res = 0

        for i in words:
            if i[:len(pref)] == pref:
                res +=1

        return res
        