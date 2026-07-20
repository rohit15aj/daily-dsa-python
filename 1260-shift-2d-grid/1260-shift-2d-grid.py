class Solution:
    def shiftGrid(self, grid, k):
        m = len(grid)
        n = len(grid[0])

        arr = []

        # Flatten the grid
        for row in grid:
            arr.extend(row)

        total = m * n
        k %= total

        # Rotate the array
        arr = arr[-k:] + arr[:-k]

        # Build the grid back
        ans = []
        idx = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[idx])
                idx += 1
            ans.append(row)

        return ans