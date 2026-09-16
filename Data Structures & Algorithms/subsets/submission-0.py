class Solution:
    def subsetRecur(self, i, nums, res, subset):
        if i == len(nums):
            res.append(subset.copy())
            return 
        
        subset.append(nums[i])
        self.subsetRecur(i+1, nums, res, subset)

        subset.pop()
        self.subsetRecur(i+1, nums, res, subset)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        res = []
        
        # finding recursively
        self.subsetRecur(0, nums, res, subset)

        return res
