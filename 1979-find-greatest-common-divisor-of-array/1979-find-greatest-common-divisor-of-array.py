class Solution:
    def findGCD(self, nums):
        mn = nums[0]
        mx = nums[0]

        for x in nums:
            if x < mn:
                mn = x
            if x > mx:
                mx = x

        ans = 1

        for d in range(1, mn + 1):
            if mn % d == 0 and mx % d == 0:
                ans = d

        return ans