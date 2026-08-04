class Solution:
    def findMissingElements(self, nums):

        mn = min(nums)
        mx = max(nums)

        seen = set(nums)
        ans = []

        for x in range(mn, mx + 1):
            if x not in seen:
                ans.append(x)

        return ans