class Solution:
    def dfs(self, coins, curr, memo): 
        #returns min num of coins at curr price
        if curr == 0:
            memo[curr] = 0
            return 0

        if curr in memo:
            return memo[curr]

        res = int(10e10)
        for coin in coins:
            tmp = curr - coin
            if tmp >= 0:
                res = min(res, 1 + self.dfs(coins, tmp, memo))
        
        memo[curr] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        #memo = {}
        #out = self.dfs(coins, amount, {})
        #return -1 if amount not in memo else out
        return -1 if self.dfs(coins, amount, {}) == int(10e10) else self.dfs(coins, amount, {})