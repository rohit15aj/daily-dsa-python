class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        memo = {}

        def dp(i, m):
            if i >= n:
                return 0

            if i + 2 * m >= n:
                return suffix[i]

            key = (i, m)

            if key in memo:
                return memo[key]

            ans = 0

            for x in range(1, 2 * m + 1):
                remaining = dp(i + x, max(m, x))
                got = suffix[i] - suffix[i + x]

                ans = max(ans, suffix[i] - remaining)

            memo[key] = ans
            return ans

        return dp(0, 1)