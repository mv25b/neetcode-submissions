class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 0
        maxS = nums[0]
        if n==1:
            return nums[0]
        for i in range(n):
            

            if curr <= 0:
                curr = 0
            curr += nums[i]
            maxS = max(maxS, curr)
        return maxS