class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007

        m = r - l + 1

        def mat_mul(A, B):
            sz = len(A)
            C = [[0] * sz for _ in range(sz)]

            for i in range(sz):
                for k in range(sz):
                    if A[i][k] == 0:
                        continue

                    aik = A[i][k]

                    for j in range(sz):
                        if B[k][j]:
                            C[i][j] = (C[i][j] + aik * B[k][j]) % MOD

            return C

        def mat_pow(M, p):
            sz = len(M)

            R = [[0] * sz for _ in range(sz)]
            for i in range(sz):
                R[i][i] = 1

            while p:
                if p & 1:
                    R = mat_mul(R, M)

                M = mat_mul(M, M)
                p >>= 1

            return R

        # U[i][j] = 1 if j < i
        U = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(i):
                U[i][j] = 1

        # D[i][j] = 1 if j > i
        D = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(i + 1, m):
                D[i][j] = 1

        UD = mat_mul(U, D)

        p = n - 1

        V = mat_pow(UD, p // 2)

        if p % 2:
            V = mat_mul(V, U)

        total = 0

        for i in range(m):
            for j in range(m):
                total = (total + V[i][j]) % MOD

        return (2 * total) % MOD
