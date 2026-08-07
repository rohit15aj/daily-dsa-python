from functools import lru_cache

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        c = [0, 0, 0, 0]
        for i, p in enumerate((2, 3, 5, 7)):
            while t % p == 0:
                c[i] += 1
                t //= p
        if t > 1:
            return "-1"
        c2, c3, c5, c7 = c

        @lru_cache(None)
        def get_min_len(r2, r3):
            r2, r3 = max(0, r2), max(0, r3)
            if not r2 and not r3:
                return 0
            res = float('inf')
            if r2:
                res = min(res, 1 + get_min_len(r2 - 1, r3), 1 + get_min_len(r2 - 2, r3), 1 + get_min_len(r2 - 3, r3))
            if r3:
                res = min(res, 1 + get_min_len(r2, r3 - 1), 1 + get_min_len(r2, r3 - 2))
            if r2 and r3:
                res = min(res, 1 + get_min_len(r2 - 1, r3 - 1))
            return res

        FACTS = [
            (0,0,0,0), (0,0,0,0), (1,0,0,0), (0,1,0,0),
            (2,0,0,0), (0,0,1,0), (1,1,0,0), (0,0,0,1),
            (3,0,0,0), (0,2,0,0)
        ]

        def can(r2, r3, r5, r7, spaces):
            return max(0, r5) + max(0, r7) + get_min_len(r2, r3) <= spaces

        def build_suffix(rem2, rem3, rem5, rem7, length):
            res = []
            for _ in range(length):
                for d in range(1, 10):
                    f2, f3, f5, f7 = FACTS[d]
                    nr2, nr3 = rem2 - f2, rem3 - f3
                    nr5, nr7 = rem5 - f5, rem7 - f7
                    if can(nr2, nr3, nr5, nr7, length - len(res) - 1):
                        res.append(str(d))
                        rem2, rem3, rem5, rem7 = nr2, nr3, nr5, nr7
                        break
            return "".join(res)

        n = len(num)
        max_prefix = num.index('0') if '0' in num else n

        prefix_factors = [(0,0,0,0)]
        p2 = p3 = p5 = p7 = 0
        for char in num:
            f2, f3, f5, f7 = FACTS[int(char)]
            p2 += f2; p3 += f3; p5 += f5; p7 += f7
            prefix_factors.append((p2, p3, p5, p7))

        for L in range(max_prefix, -1, -1):
            cp2, cp3, cp5, cp7 = prefix_factors[L]
            if L == n:
                if cp2 >= c2 and cp3 >= c3 and cp5 >= c5 and cp7 >= c7:
                    return num
                continue
            
            start_d = int(num[L]) + 1
            for d in range(start_d, 10):
                f2, f3, f5, f7 = FACTS[d]
                r2, r3 = c2 - cp2 - f2, c3 - cp3 - f3
                r5, r7 = c5 - cp5 - f5, c7 - cp7 - f7
                if can(r2, r3, r5, r7, n - 1 - L):
                    return num[:L] + str(d) + build_suffix(r2, r3, r5, r7, n - 1 - L)

        req_len = max(n + 1, c5 + c7 + get_min_len(c2, c3))
        return build_suffix(c2, c3, c5, c7, req_len)