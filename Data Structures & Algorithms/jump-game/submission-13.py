class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        push = nums[0]

        if n == 1:
            return True
        if push == 0: 
            return False
        for i in range(1,n):
            push-=1
            push = max(push, nums[i])

            if push == 0 and i != n-1:
                return False
        return True

        