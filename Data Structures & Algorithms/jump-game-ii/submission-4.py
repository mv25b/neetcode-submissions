class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        #asks what is min jumps to reach final from ith position
        #recursive - all jumps from ith position
        memo = {} #pos -> min
        def dfs(i):
            if i == n-1:
                return 0
            
            if i in memo:
                return memo[i]
            if nums[i] == 0:
                return 10e10

            end = min(n-1, i + nums[i])
            tmp_min = 10e10
            for j in range(i+1, end+1):
                tmp_min = min(tmp_min, 1 + dfs(j))
            memo[i] = tmp_min
            return tmp_min
        return dfs(0)


