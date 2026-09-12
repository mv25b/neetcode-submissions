class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1

        res = []
        while (l < r):
            tmp = numbers[l] + numbers[r]
            if (tmp == target):
                res = [l + 1, r + 1]
                break
            elif tmp < target:
                l += 1
            else:
                r-= 1
        return res