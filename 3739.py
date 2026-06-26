from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution:
    def countMajoritySubarrays(self, nums, target):

        if target not in nums:
            return 0

        prefix = [0]
        cur = 0

        for x in nums:
            if x == target:
                cur += 1
            else:
                cur -= 1
            prefix.append(cur)

        vals = sorted(set(prefix))

        bit = Fenwick(len(vals))

        ans = 0

        for p in prefix:
            idx = bisect_left(vals, p) + 1

            # previous prefix strictly smaller
            ans += bit.query(idx - 1)

            bit.update(idx, 1)

        return ans
