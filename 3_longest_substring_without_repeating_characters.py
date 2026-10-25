# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # when the set contains cabc, then meet b again, how to delete the b?
        # not sure how to deal with the above situation
        # 需要有left and right模型

        res = 0 # record the result
        left, right = 0, 0

        win = {}

        while right < len(s):
            c = s[right]
            right += 1

            # wrong syntax: win[c] = win.get(win[c], 0) + 1
            win[c] = win.get(c, 0) + 1

            #if win[c] > 1:
            while win[c] > 1:
                d = s[left]
                left += 1
                # wrong syntax: win[c] = win.get(win[c]) - 1
                # could be better: win[d] = win.get(d) - 1
                # 如果没给默认值的话，win.get(d) 就会直接崩溃，最后写成
                # 但其实不会崩溃，原因是，字典里面肯定存在，只是下面这样写更短
                win[d] -= 1
            
            res = max(res, right - left)
        
        return res
