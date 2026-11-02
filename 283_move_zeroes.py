# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Nov 1st Reviewed, PASS

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        # Nov 1st: this is 左开右闭
        # while s < len(nums):
        for i in range(slow, len(nums)):
            nums[i] = 0
