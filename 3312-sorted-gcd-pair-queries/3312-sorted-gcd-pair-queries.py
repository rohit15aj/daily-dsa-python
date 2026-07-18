from typing import List
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        P = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            multiples_count = 0
            for j in range(i, max_val + 1, i):
                multiples_count += count[j]
            P[i] = (multiples_count * (multiples_count - 1)) // 2
            
        exact_pairs = [0] * (max_val + 1)
        for i in range(max_val, 0, -1):
            exact = P[i]
            for j in range(2 * i, max_val + 1, i):
                exact -= exact_pairs[j]
            exact_pairs[i] = exact
            
        prefix_sums = [0] * (max_val + 1)
        for i in range(1, max_val + 1):
            prefix_sums[i] = prefix_sums[i - 1] + exact_pairs[i]
            
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans