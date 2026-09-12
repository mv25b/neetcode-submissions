class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp = [target - num for num in nums]

        diff = list(enumerate(tmp))
        store = {}
        for i in range(len(nums)):
            if nums[i] in store and i != store[nums[i]]:
                return [store[nums[i]], i]
            else:
                store[diff[i][1]] = diff[i][0]
        return []
        

