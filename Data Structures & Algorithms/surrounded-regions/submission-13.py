class Solution:
    def solve(self, board: List[List[str]]) -> None:
        vis = set()
        n,m = len(board), len(board[0])

        def traverse_edge():
            for i in range(m):
                dfs(0, i, True)
                dfs(n-1,i,True)

            for j in range(n):
                dfs(j,0,True)
                dfs(j,m-1,True)

        def dfs(row, col, traverse):
            if not (0 <= row < n and 0 <= col < m):
                return

            if board[row][col] == 'X' or (row,col) in vis:
                return

            vis.add((row,col))

            if not traverse:
                board[row][col] = 'X'

            dx = [0,0,1,-1]
            dy = [1,-1,0,0]

            for i in range(4):
                x = row + dx[i]
                y = col + dy[i]

                dfs(x,y,traverse)


        traverse_edge()
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j] == 'O' and (i,j) not in vis :
                    board[i][j] = 'X'
                

