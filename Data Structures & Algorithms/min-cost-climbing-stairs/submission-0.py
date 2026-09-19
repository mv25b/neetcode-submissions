class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}
        #returns min cost from num to top 
        def dfs(num):
            if num == n:
                return 0

            if num > n:
                return 10e10

            if num in memo:
                return memo[num]

            
            memo[num] = cost[num] + min(dfs(num+1), dfs(num+2))
            return memo[num]
        return min(dfs(0), dfs(1))