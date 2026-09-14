class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n, m = len(grid), len(grid[0])
        count = 0

        def dfs(i,j, grid):
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dx = [0, 0, -1, 1]
            dy = [1, -1, 0, 0]

            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x < n and 0 <= y < m:
                    if grid[x][y] == '1':
                        dfs(x, y, grid)


        for i in range (n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i,j,grid)
        return count