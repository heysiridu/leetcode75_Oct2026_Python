# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# worth to revisit

# reviewed on Oct 24th 2026
# reviewed on Nov 1st 26, PASS

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

# Reviewed on Nov 1st, look the commnets
class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ""
        i = 0
        # better way to write it for i in range(len(s)):
        while i < len(s):
            l = self.palin(s, i, i)
            r = self.palin(s, i, i + 1)

            m = l if len(m) < len(l) else m
            m = r if len(m) < len(r) else m
            
            # do not have this line
            i += 1
        
        return m

    def palin(self, s: str, l: int, r: int) -> str:
        # while s[l] == s[r] and l >= 0 and r < len(s):
        # this will cause index out of bound issues
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # return s[l + 1, r]
        return s[l + 1 : r]
