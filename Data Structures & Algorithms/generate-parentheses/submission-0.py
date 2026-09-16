class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        subset = ""
        res = []

        def dfs(open, closed, subset):
            if open == n == closed:
                res.append(subset)
                return 

            if open > closed:
                subset += ')'
                dfs(open, closed+1, subset)
                subset = subset[:-1]

            if open < n:
                subset += '('
                dfs(open+1, closed, subset)
                subset = subset[:-1]

        dfs(0,0,subset)        
        return res