class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)] 
        cols = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

       

                #0,1,2,9,10,11,18,19,20

        for n in range(3):
            for k in range(3):
                for j in range(9):
                    i = n * 3 + k
                    curr = board[j][i]
                    if curr in rows[j] or curr in cols[i] or curr in grids[3*n+ j // 3]:
                        return False
                    if curr != '.':
                        rows[j].add(curr)
                        cols[i].add(curr)
                        grids[3*n + j//3].add(curr)

        return True 