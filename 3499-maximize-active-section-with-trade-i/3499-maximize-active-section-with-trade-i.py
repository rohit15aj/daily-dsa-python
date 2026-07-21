class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count('1')

        t = '1' + s + '1'

        runs = []
        i = 0
        while i < len(t):
            j = i
            while j < len(t) and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j

        best = 0

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1' and runs[i - 1][0] == '0' and runs[i + 1][0] == '0':
                best = max(best, runs[i - 1][1] + runs[i + 1][1])

        return ones + best