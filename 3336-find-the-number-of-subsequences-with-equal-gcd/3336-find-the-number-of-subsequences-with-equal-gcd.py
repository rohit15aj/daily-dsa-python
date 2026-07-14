from math import gcd
from collections import defaultdict

class Solution:
    def subsequencePairCount(self, nums):

        MOD = 10**9 + 7

        dp = {(0, 0): 1}

        for x in nums:

            ndp = defaultdict(int)

            for (g1, g2), cnt in dp.items():

                # ignore
                ndp[(g1, g2)] = (ndp[(g1, g2)] + cnt) % MOD

                # put in seq1
                ng1 = x if g1 == 0 else gcd(g1, x)
                ndp[(ng1, g2)] = (ndp[(ng1, g2)] + cnt) % MOD

                # put in seq2
                ng2 = x if g2 == 0 else gcd(g2, x)
                ndp[(g1, ng2)] = (ndp[(g1, ng2)] + cnt) % MOD

            dp = ndp

        ans = 0

        for (g1, g2), cnt in dp.items():
            if g1 != 0 and g1 == g2:
                ans = (ans + cnt) % MOD

        return ans