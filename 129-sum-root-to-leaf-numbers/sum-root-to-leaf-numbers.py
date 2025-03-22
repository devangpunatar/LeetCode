# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, root.val)]
        res = 0

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                res += path

            if node.left:
                stack.append((node.left, path * 10 + node.left.val))
            if node.right:
                stack.append((node.right, path * 10 + node.right.val))

        return res