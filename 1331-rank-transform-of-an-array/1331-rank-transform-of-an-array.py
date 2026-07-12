class Solution:
    def arrayRankTransform(self, arr):

        rank = {}

        sorted_unique = sorted(set(arr))

        for i, num in enumerate(sorted_unique):
            rank[num] = i + 1

        return [rank[num] for num in arr]