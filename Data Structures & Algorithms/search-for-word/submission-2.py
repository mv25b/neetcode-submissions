class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board), len(board[0])

        #checks if current spot is ok 
        def valid(word, i, j):
            if -1 < i < m and -1 < j < n and board[i][j] == word[0]:
                return True
            return 

        #returns if it has valid word from curr pos 
        def traverse(word, i, j, path):
            if len(word) == 0:
                return True 

            if (i,j) in path:
                return 

            if valid(word, i, j):
                path.add((i,j))
                dx = [0,0,1,-1]
                dy = [1,-1,0,0]
                
                word = word[1:]
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if traverse(word,x,y,path):
                        return True
                path.remove((i,j))
            return 

        for i in range(m):
            for j in range(n):
                if traverse(word, i,j, set()):
                    return True

        return False