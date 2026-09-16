# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root, count):
        if not root:
            return count 
        count += 1

        left = self.dfs(root.left, count)
        right = self.dfs(root.right, count)
        return max(left, right )
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)