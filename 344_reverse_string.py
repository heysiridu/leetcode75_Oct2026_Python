# https://leetcode.com/problems/reverse-string/
# 344

class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # l = 0, r = len(s)
        l, r = 0, len(s) - 1

        while l <= r:
            # int temp = s[l]
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
