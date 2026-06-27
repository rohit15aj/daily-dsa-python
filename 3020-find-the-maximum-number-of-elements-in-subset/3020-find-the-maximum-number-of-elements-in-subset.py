from collections import Counter

class Solution:
    def maximumLength(self, nums):

        cnt = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in cnt:
            ones = cnt[1]
            if ones % 2 == 0:
                ones -= 1
            ans = max(ans, ones)

        for x in list(cnt.keys()):

            if x == 1:
                continue

            length = 0
            cur = x

            while True:

                if cur not in cnt:
                    break

                if cnt[cur] >= 2:
                    length += 2
                else:
                    length += 1
                    break

                if cur > 10 ** 9:
                    break

                nxt = cur * cur

                if nxt == cur:
                    break

                cur = nxt

            if length % 2 == 0:
                length -= 1

            ans = max(ans, length)

        return ans