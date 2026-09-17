# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        

        
        def dfs(root, max):
            if not root:
                return 0

            if root.val >= max:
                max = root.val
                return 1 + dfs(root.left, max) + dfs(root.right, max)
            return dfs(root.left, max) + dfs(root.right, max)

        return dfs(root, -200)

            