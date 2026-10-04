class Solution:
    def backtrack(self, n, k, curr, ind, res):
        if len(curr) == k:
            res.append(curr.copy())
            return 

        if ind == n:
            return 

        curr.append(ind+1)
        self.backtrack(n, k, curr, ind+1, res)
        curr.pop()
        self.backtrack(n, k, curr, ind+1, res)
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        curr = []

        self.backtrack(n, k, curr, 0, res)

        return res 