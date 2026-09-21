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
                    if tuple(curr) not in memo:
                        memo.add(tuple(curr))
                        dfs(curr,s)
                    s.remove(num)
                    curr.pop()
                    if tuple(curr) not in memo:
                        memo.add(tuple(curr))
                        dfs(curr,s)

        dfs([], set())
        return res
            