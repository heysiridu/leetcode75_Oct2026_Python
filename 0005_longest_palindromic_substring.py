# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# worth to revisit

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            s1 = self.palindrome(s, i, i)
            s2 = self.palindrome(s, i, i + 1)

            res = res if len(res) >= len(s1) else s1
            res = res if len(res) >= len(s2) else s2

        return res

    def palindrome(self, s: str, l: int, r: int) -> str:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[l + 1 : r]
