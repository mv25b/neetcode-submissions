# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head = root

        if not root or (not root.left and not root.right):
            pass
        elif not root.left:
            root.left, root.right = root.right, None
            self.invertTree(root.left)
        elif not root.right:
            root.left, root.right = None, root.left
            self.invertTree(root.right)
        elif root.left and root.right:
            root.left, root.right = root.right, root.left
            self.invertTree(root.right)
            self.invertTree(root.left)

        return head

        