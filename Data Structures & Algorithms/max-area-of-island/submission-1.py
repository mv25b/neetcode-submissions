class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_size = 0
        def dfs(i, j, grid, size):
            grid[i][j] = 0
            size += 1

            dx = [0, 0, 1, -1]
            dy = [1, -1, 0, 0]

            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]

                if -1 < x < n and -1 < y < m and grid[x][y] == 1:
                    size = dfs(x, y, grid, size)
            return size




        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    max_size = max(max_size, dfs(i, j, grid, 0))
        return max_size
