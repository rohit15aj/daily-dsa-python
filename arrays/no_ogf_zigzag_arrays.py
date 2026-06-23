class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7

        m = r - l + 1

        # up[x] = sequences ending at x where last move was up
        # down[x] = sequences ending at x where last move was down
        up = [0] * m
        down = [0] * m

        # length = 2 initialization
        for y in range(m):
            up[y] = y
            down[y] = m - 1 - y

        if n == 2:
            return m * (m - 1) % MOD

        for _ in range(3, n + 1):

            new_up = [0] * m
            new_down = [0] * m

            pref_down = [0] * (m + 1)
            for i in range(m):
                pref_down[i + 1] = (pref_down[i] + down[i]) % MOD

            suff_up = [0] * (m + 1)
            for i in range(m - 1, -1, -1):
                suff_up[i] = (suff_up[i + 1] + up[i]) % MOD

            for y in range(m):
                new_up[y] = pref_down[y]
                new_down[y] = suff_up[y + 1]

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD
