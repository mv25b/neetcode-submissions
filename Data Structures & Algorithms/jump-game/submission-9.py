class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if i == n-1:
                return True
            if dp[i] != -1:
                return dp[i]
            
            end = min(n-1, i + nums[i])
            for j in range(i+1, end+1):
                if dfs(j):
                    dp[j], dp[i] = True, True
                    return True
            dp[i] = False
            return False
        return dfs(0)
        