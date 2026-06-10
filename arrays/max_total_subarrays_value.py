import heapq
import math


class Solution(object):
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # Build Sparse Tables
        LOG = int(math.log(n, 2)) + 1

        st_max = [[0] * n for _ in range(LOG)]
        st_min = [[0] * n for _ in range(LOG)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        j = 1
        while (1 << j) <= n:
            i = 0
            while i + (1 << j) <= n:
                st_max[j][i] = max(
                    st_max[j - 1][i],
                    st_max[j - 1][i + (1 << (j - 1))]
                )

                st_min[j][i] = min(
                    st_min[j - 1][i],
                    st_min[j - 1][i + (1 << (j - 1))]
                )

                i += 1
            j += 1

        # O(1) query for max-min
        def get_value(l, r):
            j = int(math.log(r - l + 1, 2))

            mx = max(
                st_max[j][l],
                st_max[j][r - (1 << j) + 1]
            )

            mn = min(
                st_min[j][l],
                st_min[j][r - (1 << j) + 1]
            )

            return mx - mn

        # Max heap
        heap = []

        for l in range(n):
            val = get_value(l, n - 1)
            heapq.heappush(heap, (-val, l, n - 1))

        ans = 0

        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            ans += -val

            if r > l:
                new_val = get_value(l, r - 1)
                heapq.heappush(heap, (-new_val, l, r - 1))

        return ans
