from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums):

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]

            take_left = nums[i] - dp(i + 1, j)
            take_right = nums[j] - dp(i, j - 1)

            return max(take_left, take_right)

        return dp(0, len(nums) - 1) >= 0