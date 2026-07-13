class Solution:
    def sequentialDigits(self, low, high):

        ans = []

        for length in range(2, 10):

            for start in range(1, 11 - length):

                num = 0

                for d in range(start, start + length):
                    num = num * 10 + d

                if low <= num <= high:
                    ans.append(num)

        return sorted(ans)