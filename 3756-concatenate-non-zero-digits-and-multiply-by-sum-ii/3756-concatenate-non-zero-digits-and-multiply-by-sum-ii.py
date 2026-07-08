from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s, queries):
        MOD = 10 ** 9 + 7

        pos = []
        digit = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digit.append(int(ch))

        m = len(pos)

        if m == 0:
            return [0] * len(queries)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated number
        prefNum = [0] * (m + 1)
        for i in range(m):
            prefNum[i + 1] = (prefNum[i] * 10 + digit[i]) % MOD

        # prefix digit sums
        prefSum = [0] * (m + 1)
        for i in range(m):
            prefSum[i + 1] = prefSum[i] + digit[i]

        ans = []

        for l, r in queries:

            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            length = R - L + 1

            x = (prefNum[R + 1] - prefNum[L] * pow10[length]) % MOD
            sm = prefSum[R + 1] - prefSum[L]

            ans.append((x * sm) % MOD)

        return ans