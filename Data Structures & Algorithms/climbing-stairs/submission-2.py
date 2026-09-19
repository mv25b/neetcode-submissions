class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        #counts number of ways to get to n  from num
        def dfs(num):
            if num == n:
                return 1

            if num > n:
                return 0

            if memo[num] != -1:
                return memo[num]
    

            memo[num] = dfs(num+1) + dfs(num+2)
            return memo[num]
        return dfs(0)