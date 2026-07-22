from typing import List
import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Total active sections in the ENTIRE string initially
        total_ones = s.count('1')
        
        # 1. Group the string into continuous blocks/segments
        segments = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            segments.append((i, j - 1, s[i]))
            i = j

        # 2. Extract all '1'-segments and their surrounding '0'-segment boundaries
        ones_info = []
        for idx, (st, en, typ) in enumerate(segments):
            if typ == '1':
                lz_st, lz_en = -1, -1
                rz_st, rz_en = -1, -1

                if idx > 0 and segments[idx-1][2] == '0':
                    lz_st, lz_en = segments[idx-1][0], segments[idx-1][1]

                if idx < len(segments) - 1 and segments[idx+1][2] == '0':
                    rz_st, rz_en = segments[idx+1][0], segments[idx+1][1]

                ones_info.append({
                    'lz_st': lz_st, 'lz_en': lz_en,
                    'rz_st': rz_st, 'rz_en': rz_en,
                    'full_gain': (lz_en - lz_st + 1 if lz_st != -1 else 0) + \
                                 (rz_en - rz_st + 1 if rz_st != -1 else 0)
                })

        # Arrays for binary search
        L_zero_ends = []
        R_zero_starts = []
        full_gains = []
        INF = float('inf')

        for info in ones_info:
            L_zero_ends.append(info['lz_en'])
            R_zero_starts.append(info['rz_st'] if info['rz_st'] != -1 else INF)
            full_gains.append(info['full_gain'])

        # 3. Sparse Table for Range Maximum Queries (RMQ)
        K = len(full_gains)
        if K > 0:
            LOG = K.bit_length()
            st_rmq = [[0] * LOG for _ in range(K)]
            for i in range(K):
                st_rmq[i][0] = full_gains[i]

            for j in range(1, LOG):
                for i in range(K - (1 << j) + 1):
                    st_rmq[i][j] = max(st_rmq[i][j-1], st_rmq[i + (1 << (j-1))][j-1])

            def query_max(L_idx, R_idx):
                if L_idx > R_idx:
                    return 0
                j = (R_idx - L_idx + 1).bit_length() - 1
                return max(st_rmq[L_idx][j], st_rmq[R_idx - (1 << j) + 1][j])
        else:
            def query_max(L_idx, R_idx):
                return 0

        # 4. Process all queries
        ans = []
        for L, R in queries:
            if K == 0:
                ans.append(total_ones)
                continue

            # Find valid 1-segments strictly inside the left and right '0' boundaries
            k_start = bisect.bisect_left(L_zero_ends, L)
            k_end = bisect.bisect_right(R_zero_starts, R) - 1

            if k_start > k_end:
                ans.append(total_ones)
                continue

            max_gain = 0

            # Calculate partial/full gain for the first valid block (k_start)
            info = ones_info[k_start]
            gain = (info['lz_en'] - max(L, info['lz_st']) + 1) + \
                   (min(R, info['rz_en']) - info['rz_st'] + 1)
            if gain > max_gain: max_gain = gain

            # Calculate partial/full gain for the last valid block (k_end)
            if k_start != k_end:
                info = ones_info[k_end]
                gain = (info['lz_en'] - max(L, info['lz_st']) + 1) + \
                       (min(R, info['rz_en']) - info['rz_st'] + 1)
                if gain > max_gain: max_gain = gain

            # Get maximum gain from purely inside valid blocks using O(1) RMQ
            if k_start + 1 <= k_end - 1:
                mid_gain = query_max(k_start + 1, k_end - 1)
                if mid_gain > max_gain: max_gain = mid_gain

            # The answer is the original total 1s in `s` + the max gain generated in the substring
            ans.append(total_ones + max_gain)

        return ans