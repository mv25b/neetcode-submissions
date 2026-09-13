class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [10e10]*n
        dp[-1] = 0

        for i in range(n-1, -1, -1):
            end = min(n-1, nums[i] + i)

            tmp = 10e10
            for j in range(i, end + 1):
                tmp = min(tmp, 1 + dp[j])
            dp[i] = tmp
        return dp[0]-1



