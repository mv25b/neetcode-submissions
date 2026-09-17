class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        m,n = len(grid), len(grid[0])
        count = 0
        res = -1

        
    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    count += 1

        if count == 0:
            return 0
        while queue:
            for i in range (len(queue)):
                node = queue.popleft()

                dx = [0,0,1,-1]
                dy = [1,-1,0,0]

                for j in range(4):
                    x = node[0] + dx[j]
                    y = node[1] + dy[j]

                    if -1 < x < m and -1 < y < n and grid[x][y] == 1:
                        count -= 1
                        queue.append((x,y))
                        grid[x][y] = 2
            res += 1

        if count > 0:
            return -1
        return res


        