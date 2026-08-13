class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)
        tree = [None] * (4 * n)

        # [left_char, right_char, prefix, suffix, best, length]
        def make(ch):
            return [ch, ch, 1, 1, 1, 1]

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            same = (a[1] == b[0])

            prefix = a[2]
            suffix = b[3]
            best = max(a[4], b[4])

            if same:
                best = max(best, a[3] + b[2])

                if a[2] == a[5]:
                    prefix = a[5] + b[2]

                if b[3] == b[5]:
                    suffix = b[5] + a[3]

            return [
                a[0],
                b[1],
                prefix,
                suffix,
                best,
                a[5] + b[5]
            ]

        def build(node, l, r):
            if l == r:
                tree[node] = make(s[l])
                return

            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, idx, ch):
            if l == r:
                tree[node] = make(ch)
                return

            mid = (l + r) // 2

            if idx <= mid:
                update(node * 2, l, mid, idx, ch)
            else:
                update(node * 2 + 1, mid + 1, r, idx, ch)

            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        build(1, 0, n - 1)

        ans = []

        for ch, idx in zip(queryCharacters, queryIndices):
            update(1, 0, n - 1, idx, ch)
            ans.append(tree[1][4])

        return ans