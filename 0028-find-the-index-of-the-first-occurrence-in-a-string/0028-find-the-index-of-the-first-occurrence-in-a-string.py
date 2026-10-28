class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = len(needle)

        while i <= len(haystack)-len(needle):
            if haystack[i:j] == needle:
                return i
            i += 1
            j += 1
            
        return -1
        