class Solution(object):
    def longestPalindrome(self, s):
        n = len(s)
        longest = ""

        def expandaroundcenter(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        for i in range(n):
            odd_palindrome = expandaroundcenter(i, i)
            even_palindrome = expandaroundcenter(i, i+1)

            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest