class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        memo = set()

        def dfs(curr, s):
            if len(curr) == n:
                res.append(curr.copy())
                return

            for num in nums:
                if num not in s:
                    s.add(num)
                    curr.append(num)
                    dfs(curr,s)

                    s.remove(num)
                    curr.pop()

        dfs([], set())
        return res
            