class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subset = []
        res = []

        def dfs(i,sum, subset):
            if sum == target:
                res.append(subset.copy())
                return

            elif sum > target or i == len(nums):
                return 


            subset.append(nums[i])
            dfs(i, sum + nums[i], subset)

            subset.pop()
            dfs(i + 1, sum, subset)
        
        dfs(0, 0, subset)
        return res
