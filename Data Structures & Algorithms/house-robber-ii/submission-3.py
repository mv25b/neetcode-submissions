class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        #returns max money from state i 
        def dfs(i, first):
            if first and i == n-1:
                return 0
            if i >= n:
                return 0

            if (i,first) in memo:
                return memo[(i, first)]

            memo[(i,first)] = max(nums[i] + dfs(i+2, first), dfs(i+1, first))
            return memo[(i,first)]

        return max(dfs(0,True), dfs(1, False))