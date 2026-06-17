class Solution:
    def processStr(self, s, k):

        lengths = []
        curr_len = 0

        # Step 1: Track length after each operation
        for ch in s:

            if 'a' <= ch <= 'z':
                curr_len += 1

            elif ch == '*':
                if curr_len > 0:
                    curr_len -= 1

            elif ch == '#':
                curr_len *= 2

            elif ch == '%':
                pass

            lengths.append(curr_len)

        # Out of bounds
        if k >= curr_len:
            return '.'

        # Step 2: Walk backwards
        for i in range(len(s) - 1, -1, -1):

            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                # Letter added at end
                if k == curr_len - 1:
                    return ch
                curr_len -= 1

            elif ch == '*':
                # Undo remove
                curr_len += 1

            elif ch == '#':
                # Undo duplication
                half = curr_len // 2
                k %= half
                curr_len = half

            elif ch == '%':
                # Undo reverse
                k = curr_len - 1 - k

        return '.'
