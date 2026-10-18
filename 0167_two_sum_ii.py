# 167. Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # whenever an array is sorted, you should think of the two-pointer technique

        slow, fast = 0, len(numbers) - 1

        while slow < fast:
            s = numbers[slow] + numbers[fast]
            if s == target:
                return [slow + 1, fast + 1]
            elif s > target:
                fast -= 1
            else:
                slow += 1

        return [-1, -1]
